import time
import requests
import logging
from datetime import datetime
from urllib.parse import urlencode
from domain.post_dca_provider import PostDcaProvider
from domain.signature_provider import SignatureProvider
from configuration.binance_settings import BinanceSettings
from domain.exchange_settings import ExchangeSettings


class BinancePostDca(PostDcaProvider):

    # Set the default logging config as buy-YearMonth.log
    logging.basicConfig(
        filename=f"/var/log/bitcoindca/buy_{datetime.now():%Y%m}.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    def post_build_payload(
        self,
        symbol: str,
        amount: float,
        signature: SignatureProvider,
        side="BUY",
        type="MARKET",
    ):
        """This method build the payload with the signature provider

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

        payload["signature"] = signature.sign(urlencode(payload))

        return payload

    # TODO Replace float
    def post(self, amount, signature: SignatureProvider, symbol="BTCUSDT"):
        
        
        exchange_settings: ExchangeSettings = BinanceSettings()

        binance_settings = exchange_settings.settings()

        full_url = (
            f"{binance_settings['base_url']}{binance_settings['endpoints']['order']}"
        )

        payload = self.post_build_payload(symbol, amount, signature)

        logging.info(f"Sending {full_url} as {payload['side']} post request")

        # req = requests.post(
        #     full_url
        #     , headers={
        #     "X-MBX-APIKEY":API_KEY,
        #     }
        #     , params = payload)

        # if(req.status_code == 200):
        #     resp_as_json = req.json()
        #     symbol = resp_as_json['symbol']

        #     order_status = resp_as_json['status']
        #     order_id = resp_as_json['orderId']

        #     logging.info(f"Market order filled at {symbol} successfully with status {order_status} with the order id {order_id}")
        #     get_user_balance()
        # else:
        #     logging.error(f"Failed to post market order : {req.text}")

    def get_user_balances(self):
        user_balance_params = {"timestamp": int(time.time() * 1000)}

        user_balance_params["signature"] = create_hmac_signature(user_balance_params)

        headers = {
            "X-MBX-APIKEY": API_KEY,
        }

        req = requests.get(
            f"{CURRENT_URL}{USER_INFO_ENDPOINT}",
            params=user_balance_params,
            headers=headers,
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
