import argparse, os , datetime

def build_script_args():
    api_key = 'api_key' #os.getenv('BINANCE_API_KEY')
    #secret_key = os.getenv('BINANCE_SECRET_KEY')
    print(api_key)
    if not api_key :#or not secret_key:
        raise ValueError("API key and Secret key must be set in environment variables.")

    parser = argparse.ArgumentParser(description='Binance DCA for Bitcoin')

    parser.add_argument('-M', '--monthly',
        required=False,
        help='Run monthly DCA script on the current day.',
        action='store_true'
    )

    parser.add_argument(
        '-D', '--day',
        required=False,
        nargs=1,
        type=int,
        help='Day of the month. Must be used with --monthly flag. Defaults to current day if not provided.'
    )

    parser.add_argument(
        '-Ew', '--every-week-day',
        required=False,
        nargs=1,
        type=int,
        help='Day of the week to invest (0=Monday, 6=Sunday). Defaults to current weekday if not provided.'
    )

    parser.add_argument(
        '-A','--amount',
        type=float,
        required=True,
        help='Amount in USDT to invest each interval '
    )

    args = parser.parse_args()

    # Monthly validation   

    if args.day and not args.monthly:
        parser.error("--day can only be used with --monthly (-M) flag.")

    if args.monthly and not args.day:
        args.day = [datetime.datetime.now().day]

    if args.day[0] < 1 or args.day[0] > 28:
        parser.error("Day must be between 1 and 28 to avoid issues with February.")

    # Paramteres conflict validation
    if args.monthly and args.every_week_day:
        parser.error("Cannot use --monthly (-M) and --every-week-day (-Ew) flags together.")

    return args