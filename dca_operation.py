import argparse
import logging
import requests
import hmac
import hashlib
import time
import os
import dotenv
from datetime import datetime
from urllib.parse import urlencode

ORDER_ENDPOINT="/api/v3/order"
USER_INFO_ENDPOINT="/api/v3/account"
ENV_KEYS_FILE="/etc/default/btcdca/secrets"
CURRENT_URL= "https://api.binance.com" 
#CURRENT_URL="https://testnet.binance.vision/api" -> TESTNET
SECRET_KEY=None
API_KEY=None

logging.basicConfig(
    filename=f'/var/log/bitcoindca/buy_{datetime.now():%Y%m}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def configure_arguments():
    parser = argparse.ArgumentParser(description='Binance DCA for Bitcoin')

    parser.add_argument(
        '-A','--amount',
        help="The amount of USDT",
        type=int,
        required=True
    )

    return parser.parse_args()

def create_hmac_signature(parameters):
    return hmac.new(
        SECRET_KEY.encode(),
        urlencode(parameters).encode(),
        hashlib.sha256
    ).hexdigest()
    

def post_dca(amount):

    paramsConfig = {
        "side":"BUY",
        "symbol":"BTCUSDT",
        "type":"MARKET",
        "quoteOrderQty":amount,
        "timestamp":int(time.time() * 1000)
    }
    full_url=f'{CURRENT_URL}{ORDER_ENDPOINT}'

    headers={
        "X-MBX-APIKEY":API_KEY,
    }

    paramsConfig['signature'] = create_hmac_signature(paramsConfig)


    logging.info(f"Sending {full_url} as {paramsConfig['side']} post request")
    
    req = requests.post(full_url, headers=headers, params = paramsConfig)

    if(req.status_code == 200):
        resp_as_json = req.json()
        symbol = resp_as_json['symbol']

        order_status = resp_as_json['status']
        order_id = resp_as_json['orderId']

        logging.info(f"Market order filled at {symbol} successfully with status {order_status} with the order id {order_id}")
        get_user_balance()
    else:
        logging.error(f"Failed to post market order : {req.text}")

def get_user_balance():
    user_balance_params = {
        'timestamp':int(time.time() * 1000)
    }

    user_balance_params['signature'] = create_hmac_signature(user_balance_params)

    headers={
        "X-MBX-APIKEY":API_KEY,
    }

    req = requests.get(f'{CURRENT_URL}{USER_INFO_ENDPOINT}',
        params=user_balance_params,
        headers=headers
    )

    if(req.status_code == 200):
        balances = req.json()['balances']
        if balances:
            btc_balance = [asset for asset in balances if asset['asset'] == 'BTC']
            usdt_balance = [asset for asset in balances if asset['asset'] == 'USDT']

            if not btc_balance or not usdt_balance:
                logging.error(f"Error retrieving balances. There's not an usdt_balance or btc_balance")
                raise Exception("Error retrieving balances")
            
            btc_and_usdt_balance = {
                "BTC":btc_balance[0]['free'],
                "USDT":usdt_balance[0]['free']
            }

            logging.info(f"User balances retrieved successfully {btc_and_usdt_balance} ")

            return btc_and_usdt_balance
    else:
        logging.error(f"Error to retrieve user account information with status code {req.status_code}")

if __name__ == '__main__':
    dotenv.load_dotenv(ENV_KEYS_FILE)
    SECRET_KEY=os.getenv("SECRET_KEY").replace("\"","")
    API_KEY=os.getenv("API_KEY").replace("\"","")
    argument = configure_arguments()
    
    post_dca(argument.amount)
    
    # To do : Add telegram bot message after every buy
    

