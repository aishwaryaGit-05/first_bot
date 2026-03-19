from data_collector import get_price_data
from strategy_bot import moving_average_strategy
from execution import execute_trade
from config import SYMBOLS, POSITION_SIZE

for symbol in SYMBOLS:

    data = get_price_data(symbol)

    signal = moving_average_strategy(data)

    if signal != "HOLD":
        execute_trade(symbol, signal, POSITION_SIZE)