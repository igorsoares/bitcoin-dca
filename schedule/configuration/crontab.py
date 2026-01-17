from schedule.configuration.setup_config_env import getenvs

def create_crontab(cron:str, amount:float):
    try:
        config_envs = getenvs()['config']
        opt_dir = config_envs['opt-directory']
        crontab_file = config_envs['crontab-file']
        
        full_expression = f'{cron} root cd {opt_dir} && ./venv/bin/python3 -m schedule.dca_operation --amount {amount}'
        with open(crontab_file, 'w') as cronfile:
            cronfile.write(f'{full_expression}\n')
        print("[+] Your Bitcoin DCA has been successfully created and is already running.")
    except Exception as e:
        print("[-] Failed to write to cron file configuration. ", e)
        raise e
    


