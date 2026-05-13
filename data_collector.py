import yfinance as yf
import pandas as pd

def get_price_data(symbol):
    data = yf.download(symbol, period="3mo", interval="1d") # symbol means the stock symbol, e.g., "AAPL" for Apple Inc.
    if data.columns.nlevels > 1:
        data.columns = data.columns.droplevel(1)
        print("Dropped multi-level columns:", data.columns)
    return data