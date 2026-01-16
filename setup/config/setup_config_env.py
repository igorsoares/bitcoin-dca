"""
Centralized configurations for initial Setup
"""
class SetupConfig:
    # Main DCA operation script name and directories
    OPT_DIR="/opt/bitcoindca"
    ETC_SECRETS_DIR = "/etc/default/bitcoindca/"
    LOG_DIR = "/var/log/bitcoindca/"
    SECRET_FILE_PERMISSION=0o600

    # Crontab file path
    CRONTAB_FILE = "/etc/cron.d/bitcoin"

    # Binance API key generation documentation
    BINANCE_GENERATE_TOKENS_DOC = "https://www.binance.com/en/support/faq/detail/360002502072"

    # Print colors
    YELLOW = "\033[33m"
    GREEN = '\033[32m'
    RESET = "\033[0m"