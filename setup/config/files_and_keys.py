import subprocess
import os 
from getpass import getpass

DCA_OPERATION_SCRIPT_NAME="dca_operation.py"
ETC_SECRETS_DIR = "/etc/default/btcdca/"
LOG_DIR = "/var/log/bitcoindca/"
BINANCE_GENERATE_TOKENS_DOC = "https://www.binance.com/en/support/faq/detail/360002502072"

def _api_keys_setup():
    try:
        print(f"If you don’t have a Binance API key or secret key, please read this. {BINANCE_GENERATE_TOKENS_DOC}")
        secret_key_in = str(getpass("Please inform the secret key: "))
        api_key_in = str(getpass("Please inform the api key: "))
        os.makedirs(ETC_SECRETS_DIR, exist_ok=True)
        
        full_secret_path=ETC_SECRETS_DIR + "secrets"

        with open(full_secret_path,"w") as secrets_file:
            secrets_file.write(f"SECRET_KEY={secret_key_in}\n")
            secrets_file.write(f"API_KEY={api_key_in}\n")

        subprocess.run(["chmod","600",full_secret_path], check=True)
    except Exception as e:
        raise e

def create_log_directory():
    os.makedirs(LOG_DIR, exist_ok=True)

def copy_main_dca_script():
    full_path = f'/usr/local/bin/{DCA_OPERATION_SCRIPT_NAME}' 
    subprocess.run(["cp","./dca_operation.py",full_path],check=True)

def setup_files():
    try:
        _api_keys_setup()

        create_log_directory()
        
        copy_main_dca_script()
    except subprocess.CalledProcessError as e:
        raise e;