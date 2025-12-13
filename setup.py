# Execute as sudo
from setup.domain.every_month_cron import EveryMonth
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
    print("Weekly buy")

def menu():
    print(banner())

    menu_actions = {
        1: monthly_build
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
        
        create_crontab(menu_actions[option]())
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


