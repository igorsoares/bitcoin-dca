from domain.exchange_settings import ExchangeSettings
from pathlib import Path
import configuration.user_environment as user_environment
import yaml

class BinanceSettings(ExchangeSettings):
    
    def settings(self):
        with open(Path(user_environment.settings_yaml_file), "r", encoding="utf-8") as file:
            return yaml.safe_load(file)['binance']
