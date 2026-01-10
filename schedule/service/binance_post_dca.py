import time
import requests
import logging
from decimal import Decimal
from datetime import datetime
from urllib.parse import urlencode, urljoin
from domain.post_dca_provider import PostDcaProvider
from domain.signature_provider import SignatureProvider
from configuration.binance_settings import BinanceSettings
from domain.exchange_settings import ExchangeSettings

# Set the default logging config as buy-YearMonth.log
logging.basicConfig(
    filename=f"/var/log/bitcoindca/buy_{datetime.now():%Y%m}.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class BinancePostDca(PostDcaProvider):

    def __init__(
        self, signature: SignatureProvider, exchange_settings: ExchangeSettings, secrets
    ):
        self.signature = signature
        self.secrets = secrets
        self.exchange_settings = exchange_settings

    def _build_header(self):
        return {"X-MBX-APIKEY": self.secrets["api_key"]}

    def _sign_payload(self, payload: dict) -> dict:
        payload["signature"] = self.signature.sign(urlencode(payload))
        return payload

    def _parse_order_response(self, resp: dict) -> dict:
        return {
            "symbol": resp["symbol"],
            "order_status": resp["status"],
            "order_id": resp["orderId"],
            "quote_qty": resp["cummulativeQuoteQty"],
            "btc_qty": resp["executedQty"],
        }

    def _post_build_payload(
        self,
        symbol: str,
        amount: float,
        side="BUY",
        type="MARKET",
    ):
        """This method build the post market order payload with the signature provider

        Args:
            symbol (str): The asset symbol.
            amount (float): Amount in
            side (str, optional): Buy or Sell. Defaults to "BUY".
            type (str, optional): Order type (MARKET / LIMIT). Defaults to "MARKET".

        Returns:
            dict: A complete payload with the signature included
        """

        payload = {
            "side": side,
            "symbol": symbol,
            "type": type,
            "quoteOrderQty": amount,
            "timestamp": int(time.time() * 1000),
        }

        self._sign_payload(payload)

        return payload

    def post(self, amount: Decimal, symbol="BTCUSDT"):
        try:

            binance_settings = self.exchange_settings.settings()

            full_url = urljoin(
                binance_settings["base_url"], binance_settings["endpoints"]["order"]
            )

            payload = self._post_build_payload(symbol, amount)

            logging.info(f"Sending {full_url} as {payload['side']} request")

            req = requests.post(
                full_url, headers=self._build_header(), params=payload, timeout=20
            )

            if req.status_code == 200:
                resp_as_json = req.json()

                order_response = self._parse_order_response(resp_as_json)

                log_message = f"""Market order filled at {symbol} successfully with status {order_response['order_status']}
        order id: {order_response['order_id']}
        quote_qty: {order_response['quote_qty']}
        btc_qty: {order_response['btc_qty']}                
                """

                logging.info(log_message)

                self.get_user_balances()

            else:
                logging.error(f"Failed to post market order : {req.text}")
        except requests.exceptions.RequestException as reqExc:
            logging.exception("Error posting market order to Binance")
            raise

    def get_user_balances(self):
        binance_settings = self.exchange_settings.settings()

        full_url = urljoin(
            binance_settings["base_url"], binance_settings["endpoints"]["account"]
        )

        user_balance_params = {"timestamp": int(time.time() * 1000)}

        self._sign_payload(user_balance_params)

        req = requests.get(
            full_url,
            params=user_balance_params,
            headers=self._build_header(),
        )

        if req.status_code == 200:
            balances = req.json()["balances"]
            if balances:
                btc_balance = [asset for asset in balances if asset["asset"] == "BTC"]
                usdt_balance = [asset for asset in balances if asset["asset"] == "USDT"]

                if not btc_balance or not usdt_balance:
                    logging.error(
                        f"Error retrieving balances. There's not an usdt_balance or btc_balance"
                    )
                    raise Exception("Error retrieving balances")

                btc_and_usdt_balance = {
                    "BTC": btc_balance[0]["free"],
                    "USDT": usdt_balance[0]["free"],
                }

                logging.info(
                    f"User balances retrieved successfully {btc_and_usdt_balance} "
                )

                return btc_and_usdt_balance
        else:
            logging.error(
                f"Error to retrieve user account information with status code {req.status_code}"
            )
