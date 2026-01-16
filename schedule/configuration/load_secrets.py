from dotenv import load_dotenv
from os import getenv
from sys import exit
from config import settings
import configuration.user_environment as user_environment


def load():
    try:
        
        #load_dotenv(SetupConfig.ETC_SECRETS_DIR+"secrets")

        return {
            "secret_key": getenv("SECRET_KEY"),
            "api_key": getenv("API_KEY")
        }
    except Exception as e:
        print("[-] Failed to load secrets. Check your software version or permissions. ", e)
        exit(1)