from .setup_config_env import SetupConfig

def create_crontab(cron:str, amount:float):
    try:
        dca_operation_file=f"{SetupConfig.OPT_DIR}/schedule/dca_operation.py"
        python_venv_bin=f"{SetupConfig.OPT_DIR}/venv/bin/python3"

        full_expression = f'{cron} root {python_venv_bin} {dca_operation_file} --amount {amount}'
        with open(SetupConfig.CRONTAB_FILE, 'w') as cronfile:
            cronfile.write(f'{full_expression}\n')
        print("[+] Your Bitcoin DCA has been successfully created and is already running.")
    except Exception as e:
        print("[-] Failed to write to cron file configuration. ", e)
        raise e
    


