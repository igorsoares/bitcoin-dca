#!/opt/bitcoind-dca/venv/bin/python
from configuration.arguments import configure_arguments
from configuration.load_secrets import load
from service.binance_post_dca import BinancePostDca
from service.hmac_signature import HmacSignature
from domain.signature_provider import SignatureProvider

if __name__ == "__main__":
    arguments = configure_arguments()
    amount = arguments.amount

    binance_post: BinancePostDca = BinancePostDca()
    hmac_algo: SignatureProvider = HmacSignature(load()["secret_key"])

    binance_post.post(amount, hmac_algo)
