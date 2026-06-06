import streamlit as st
# import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from config import API_KEY, SECRET_KEY, BASE_URL


trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
account = trading_client.get_account()


col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Portfolio Value",
    f"${float(account.portfolio_value):,.2f}"
)

col2.metric(
    "Cash",
    f"${float(account.cash):,.2f}"
)

col3.metric(
    "Buying Power",
    f"${float(account.buying_power):,.2f}"
)

col4.metric(
    "Equity",
    f"${float(account.equity):,.2f}"
)