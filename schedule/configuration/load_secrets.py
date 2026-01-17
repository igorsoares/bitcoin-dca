from dotenv import load_dotenv
from os import getenv
from sys import exit
from schedule.configuration.setup_config_env import getenvs

def load():
    try:
        config = getenvs()
        load_dotenv(f"{config['config']['secrets-file']}")

        return {
            "secret_key": getenv("SECRET_KEY"),
            "api_key": getenv("API_KEY")
        }
    except Exception as e:
        print("[-] Failed to load secrets. Check your software version or permissions. ", e)
        exit(1)