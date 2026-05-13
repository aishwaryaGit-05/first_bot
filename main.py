from data_collector import get_price_data
from strategy_bot import get_strategy_data, improved_strategy
from execution import execute_trade
from config import BASE_URL, SECRET_KEY, SYMBOLS, POSITION_SIZE, API_KEY
import alpaca_trade_api as tradeapi
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

def run_trades():
    print("Running trades...")
    trade_history = []
    for symbol in SYMBOLS:
        try:
            position = api.get_position(symbol)
        except:
            position = None
        data = get_price_data(symbol)
        signal = get_strategy_data(data, position)
        if signal != "HOLD":
            trade_history.append(execute_trade(symbol, signal, POSITION_SIZE))
    return trade_history


if __name__ == "__main__":
    run_trades()

# def get_main_data():
#     """
#     Returns main data as a DataFrame
#     """
#     # Replace with your actual data retrieval logic
#     # Example:
#     import pandas as pd
#     main_data = pd.DataFrame({
#         "Column1": [...],
#         "Column2": [...],
#     })
#     return main_data