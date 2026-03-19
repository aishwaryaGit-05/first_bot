# Stores trading activity.

import datetime

def log_trade(action, symbol):

    with open("trades.log", "a") as f:
        f.write(f"{datetime.datetime.now()} {action} {symbol}\n")

# This helps analyze performance later.