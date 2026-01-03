from domain.exchange_settings import ExchangeSettings
from pathlib import Path
import yaml

class BinanceSettings(ExchangeSettings):
    
    def settings(self, path="settings.yaml"):
        with open(Path(path), "r", encoding="utf-8") as file:
            return yaml.safe_load(file)['binance']
