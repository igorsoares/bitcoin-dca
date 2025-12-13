#!/opt/bitcoind-dca/venv/bin/python
from setup.domain.every_month_cron import EveryMonth
from setup.domain.every_week_day_cron import EveryWeekDay
from setup.config.crontab import create_crontab
from setup.config.files_and_keys import *
import sys

def banner():
    return """

██████╗ ██╗████████╗ ██████╗ ██████╗ ██╗███╗   ██╗    ██████╗  ██████╗ █████╗ 
██╔══██╗██║╚══██╔══╝██╔════╝██╔═══██╗██║████╗  ██║    ██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║   ██║     ██║   ██║██║██╔██╗ ██║    ██║  ██║██║     ███████║
██╔══██╗██║   ██║   ██║     ██║   ██║██║██║╚██╗██║    ██║  ██║██║     ██╔══██║
██████╔╝██║   ██║   ╚██████╗╚██████╔╝██║██║ ╚████║    ██████╔╝╚██████╗██║  ██║
╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝
"""


def monthly_build():
    every_month = EveryMonth()
    return every_month.build()

def weekly_buy():
    every_week_day = EveryWeekDay()
    return every_week_day.build()

def menu():
    print(banner())

    menu_actions = {
        1: monthly_build,
        2: weekly_buy
    }
    
    print("""
        1. Configure monthly buy
        2. Configure weekly buy
        0. Exit       
    """)
    try:
        option = int(input("Select: "))
        if option == 0:
            return
        
        amount = float(input("Amount in USD: "))

        if amount < 0:
            raise Exception("Invalid amount value")

        cron_expression = menu_actions[option]()

        create_crontab(cron_expression, amount)
    except Exception as e:
        print(f"Goodbye. {e}")



if __name__ == '__main__':
    try:
        if os.geteuid() != 0:
            print("This script must be run as root or with sudo.")
            sys.exit(1)
        setup_files()
        menu()
    except Exception as e:
        print(f"Failed to setup configuration: {e}")


