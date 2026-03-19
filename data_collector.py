import yfinance as yf
import pandas as pd

def get_price_data(symbol):
    data = yf.download(symbol, period="3mo", interval="1d")
    if data.columns.nlevels > 1:
        data.columns = data.columns.droplevel(1)
    return data