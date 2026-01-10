import os 
from sys import exit
from getpass import getpass
from .setup_config_env import SetupConfig

def print_colored(message: str, color_code: str = SetupConfig.RESET):
    print(f"{color_code}{message}{SetupConfig.RESET}")

def _clear_console():
    os.system("clear")

def _api_keys_setup():
    try:
        print_colored(f"[ALERT] If you don’t have a Binance API key, read: {SetupConfig.BINANCE_GENERATE_TOKENS_DOC}", SetupConfig.YELLOW)

        secret_key_in = str(getpass("Enter the secret key: "))
        api_key_in = str(getpass("Enter the api key: "))
        os.makedirs(SetupConfig.ETC_SECRETS_DIR, exist_ok=True)
        
        full_secret_path= os.path.join(SetupConfig.ETC_SECRETS_DIR, "secrets")

        with open(full_secret_path,"w") as secrets_file:
            secrets_file.write(f"SECRET_KEY={secret_key_in}\n")
            secrets_file.write(f"API_KEY={api_key_in}\n")

        os.chmod(full_secret_path, SetupConfig.SECRET_FILE_PERMISSION)
    except Exception as exception:
        print("[-] Failed to setup API Keys: ", exception)
        exit(1)

def setup_files():
    _clear_console()
    _api_keys_setup()


if __name__ == "__main__":
    setup_files()