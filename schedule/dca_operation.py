#!/opt/bitcoind-dca/venv/bin/python
from configuration.arguments import configure_arguments
from configuration.load_secrets import load
from configuration.binance_settings import BinanceSettings
from service.binance_post_dca import BinancePostDca
from service.hmac_signature import HmacSignature
from domain.signature_provider import SignatureProvider

if __name__ == "__main__":
    arguments = configure_arguments()
    amount = arguments.amount

    secrets = load()

    hmac_algo: SignatureProvider = HmacSignature(secrets["secret_key"])
    
    binance_post: BinancePostDca = BinancePostDca(hmac_algo, BinanceSettings(), secrets )
    binance_post.post(amount)
