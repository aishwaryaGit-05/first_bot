# import yfinance as yf
# # import pandas as pd

# def get_price_data(symbol):
#     data = yf.download(symbol, period="3mo", interval="1d") # symbol means the stock symbol, e.g., "AAPL" for Apple Inc.
#     if data.columns.nlevels > 1:
#         data.columns = data.columns.droplevel(1)
#         print("Dropped multi-level columns:", data.columns)
#     return data

from alpaca.data.historical.stock import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.enums import DataFeed

from datetime import datetime, timedelta
import pandas as pd

from config import API_KEY, SECRET_KEY, BASE_URL


client = StockHistoricalDataClient(API_KEY, SECRET_KEY)


def get_price_data(symbol):

    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)

    request_params = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Day,
        start=datetime.now() - timedelta(days=90),
        feed=DataFeed.IEX   # IMPORTANT
    )

    bars = client.get_stock_bars(request_params)

    data = bars.df

    # reset index for easier dataframe handling
    data = data.reset_index()

    return data