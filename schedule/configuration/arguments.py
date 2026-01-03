import argparse
from sys import exit

def parameters_validation(parser):
    amount = parser.amount
    
    if amount < 0:
        print(f"[-] Invalid amount parameter : {amount}")
        exit(1)

def configure_arguments():
    parser = argparse.ArgumentParser(description='Binance DCA for Bitcoin')

    parser.add_argument(
        '-A','--amount',
        help="The amount of USDT to spend",
        type=float,
        required=True
    )
    
    args = parser.parse_args()
    
    parameters_validation(args)

    return args