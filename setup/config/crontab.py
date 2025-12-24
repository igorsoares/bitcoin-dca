import logging
from .setup_config_env import SetupConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_crontab(cron:str, amount:float):
    try:
        full_expression = f'{cron} root /usr/local/bin/dca_operation.py --amount {amount}'
        with open(SetupConfig.CRONTAB_FILE, 'w') as cronfile:
            cronfile.write(f'{full_expression}\n')
        logging.info("Crontab file created successfully.")
    except Exception as e:
        logging.error("Failed to write to cron file configuration")
        raise e
    


