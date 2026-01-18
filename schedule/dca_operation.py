#!/opt/bitcoind-dca/venv/bin/python
from schedule.configuration.arguments import configure_arguments
from schedule.configuration.load_secrets import load
from schedule.domain.models.binance_settings import BinanceSettings
from schedule.service.binance_post_dca import BinancePostDca
from schedule.service.hmac_signature import HmacSignature
from schedule.domain.interfaces.signature_provider import SignatureProvider

if __name__ == "__main__":
    arguments = configure_arguments()
    amount = arguments.amount

    secrets = load()

    hmac_algo: SignatureProvider = HmacSignature(secrets["secret_key"])
    
    binance_post: BinancePostDca = BinancePostDca(hmac_algo, BinanceSettings(), secrets )
    binance_post.post(amount)
