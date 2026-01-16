#!/opt/bitcoind-dca/venv/bin/python
from domain.every_month_cron import EveryMonth
from domain.every_week_day_cron import EveryWeekDay
from config.crontab import create_crontab
from config.files_and_keys import *
from config.setup_config_env import SetupConfig
import sys

def banner():
    print(f"""
{SetupConfig.GREEN}
██████╗ ██╗████████╗ ██████╗ ██████╗ ██╗███╗   ██╗    ██████╗  ██████╗ █████╗ 
██╔══██╗██║╚══██╔══╝██╔════╝██╔═══██╗██║████╗  ██║    ██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║   ██║     ██║   ██║██║██╔██╗ ██║    ██║  ██║██║     ███████║
██╔══██╗██║   ██║   ██║     ██║   ██║██║██║╚██╗██║    ██║  ██║██║     ██╔══██║
██████╔╝██║   ██║   ╚██████╗╚██████╔╝██║██║ ╚████║    ██████╔╝╚██████╗██║  ██║
╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝
{SetupConfig.RESET}
""")


def monthly_build():
    every_month = EveryMonth()
    return every_month.build()

def weekly_buy():
    every_week_day = EveryWeekDay()
    return every_week_day.build()

def menu():
    banner()

    menu_actions = {
        1: monthly_build,
        2: weekly_buy
    }
    
    print("""
        [1] Configure monthly buy
        [2] Configure weekly buy
        [0] Exit
    """)
    try:
        option = int(input("Select: "))
        if option == 0:
            return
        
        amount = float(input("Amount in USD: "))

        if amount < 0:
            raise Exception("Invalid amount value")

        chose_action = menu_actions[option]

        create_crontab(chose_action(), amount)
    except Exception as e:
        print("Invalid input. Goodbye.")
        sys.exit(1)


if __name__ == '__main__':
    try:
        if os.geteuid() != 0:
            print("This script must be run as sudo.")
            sys.exit(1)
        setup_files()
        menu()
    except Exception as e:
        print(f"Failed to setup configuration: {e}")


