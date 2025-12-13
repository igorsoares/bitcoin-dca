from pathlib import Path
from ..domain.cron import Cron

CRONTAB_FILE = "/etc/cron.d/bitcoin"

# For now, only one crontab file per configuration
def create_crontab(cron:str):
    try:
        full_expression = f'{cron} root python3 /usr/local/bin/dca_operation.py'
        with open(CRONTAB_FILE, 'w') as cronfile:
            cronfile.write(full_expression)
        print("Crontab file created successfully.")
    except Exception as e:
        print("Failed to write to cron file configuration")
        raise e
    


