import subprocess
import os 
import logging
from getpass import getpass
from .setup_config_env import SetupConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def print_colored(message: str, color_code: str = SetupConfig.RESET):
    print(f"{color_code}{message}{SetupConfig.RESET}")


def _api_keys_setup():
    try:
        print_colored(f"[ALERT] If you don’t have a Binance API key, read: ", SetupConfig.YELLOW)
        print(SetupConfig.BINANCE_GENERATE_TOKENS_DOC)

        secret_key_in = str(getpass("Enter the secret key: "))
        api_key_in = str(getpass("Enter the api key: "))
        os.makedirs(SetupConfig.ETC_SECRETS_DIR, exist_ok=True)
        
        full_secret_path= os.path.join(SetupConfig.ETC_SECRETS_DIR, "secrets")

        with open(full_secret_path,"w") as secrets_file:
            secrets_file.write(f"SECRET_KEY={secret_key_in}\n")
            secrets_file.write(f"API_KEY={api_key_in}\n")

        os.chmod(full_secret_path, SetupConfig.SECRET_FILE_PERMISSION)
    except Exception as e:
        raise e

def _create_log_directory():
    logging.info("Creating log directory")
    os.makedirs(SetupConfig.LOG_DIR, exist_ok=True)

def _copy_main_dca_script():
    logging.info("Copying DCA script to /usr/local/bin")
    full_path = os.path.join('/usr/local/bin', SetupConfig.DCA_OPERATION_SCRIPT_NAME)
    subprocess.run(["cp","schedule/dca_operation.py",full_path],check=True)

def setup_files():
    _api_keys_setup()

    _create_log_directory()
    
    _copy_main_dca_script()


if __name__ == "__main__":
    setup_files()