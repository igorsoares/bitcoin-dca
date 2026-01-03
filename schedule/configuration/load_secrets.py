from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from sys import exit
import yaml

def load(path:str="settings.yaml"):
    try:
        configs = None
        with open(Path(path), "r", encoding="utf-8") as file:
            configs = yaml.safe_load(file)['config']
        load_dotenv(configs['secrets'])

        return {
            "secret_key": getenv("SECRET_KEY"),
            "api_key": getenv("API_KEY")
        }
    except Exception as e:
        print("[-] Failed to load secrets. Check your software version or permissions. ", e)
        exit(1)