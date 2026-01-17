import os 
from sys import exit
from getpass import getpass
from schedule.common import utils
from schedule.configuration.setup_config_env import getenvs

def _api_keys_setup():
    try:
        configs_env = getenvs()['config']
        binance_envs = getenvs()['binance']
        secrets_directory = configs_env['secrets-directory']
        full_secrets_file = f"{secrets_directory}/secrets"

        utils.print_yellow(f"[ALERT] If you don’t have a Binance API key, read: {binance_envs['generate-tokens-doc']}")

        secret_key_in = str(getpass("Enter the secret key: "))
        api_key_in = str(getpass("Enter the api key: "))
        os.makedirs(secrets_directory, exist_ok=True)
        
        with open(full_secrets_file,"w") as secrets_file:
            secrets_file.write(f"SECRET_KEY={secret_key_in}\n")
            secrets_file.write(f"API_KEY={api_key_in}\n")

        os.chmod(full_secrets_file, 0o600)
    except Exception as exception:
        print("[-] Failed to setup API Keys: ", exception)
        exit(1)

def setup_files():
    utils.clear_console()
    _api_keys_setup()


if __name__ == "__main__":
    setup_files()