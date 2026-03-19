import alpaca_trade_api as tradeapi
from config import API_KEY, SECRET_KEY, BASE_URL

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

def execute_trade(symbol, action, qty):

    if action == "BUY":
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )

    elif action == "SELL":
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )