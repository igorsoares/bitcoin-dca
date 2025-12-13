from pathlib import Path
from ..domain.cron import Cron

CRONTAB_FILE = "/etc/cron.d/bitcoin"

# For now, only one crontab file per configuration
def create_crontab(cron:str, amount:float):
    try:
        full_expression = f'{cron} root sudo /usr/local/bin/dca_operation.py --amount {amount}'
        with open(CRONTAB_FILE, 'w') as cronfile:
            cronfile.write(f'{full_expression}\n')
        print("Crontab file created successfully.")
    except Exception as e:
        print("Failed to write to cron file configuration")
        raise e
    


