import argparse
from sys import exit
import schedule.configuration.user_environment as user_environment


def _parameters_validation(parser):
    amount = parser.amount

    if amount < 0:
        print(f"[-] Invalid amount parameter : {amount}")
        exit(1)
        
    user_environment.settings_yaml_file = 'settings.yaml'
    
    if parser.env == 'dev':
        user_environment.settings_yaml_file = 'settings-dev.yaml'
    

def configure_arguments():
    parser = argparse.ArgumentParser(description="Binance DCA for Bitcoin")

    parser.add_argument(
        "-A", "--amount", help="The amount of USDT to spend", type=float, required=True
    )

    parser.add_argument(
        "--env",
        help="Execution environment",
        default="prod",
        choices=["prod", "dev"],
        required=False,
    )

    args = parser.parse_args()

    _parameters_validation(args)

    return args
