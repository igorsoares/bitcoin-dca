from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from sys import exit
import configuration.user_environment as user_environment
import yaml

def load():
    try:
        with open(Path(user_environment.settings_yaml_file), "r", encoding="utf-8") as file:
            configs = yaml.safe_load(file)['config']
        load_dotenv(configs['secrets'])

        return {
            "secret_key": getenv("SECRET_KEY"),
            "api_key": getenv("API_KEY")
        }
    except Exception as e:
        print("[-] Failed to load secrets. Check your software version or permissions. ", e)
        exit(1)