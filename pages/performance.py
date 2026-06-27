from alpaca.trading.client import TradingClient
from config import API_KEY, SECRET_KEY, BASE_URL
import streamlit as st
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
import pandas as pd
from alpaca.trading.requests import GetPortfolioHistoryRequest
import plotly.express as px
from components.sidebar import show_sidebar


if not st.session_state.get("logged_in"):
    st.switch_page("dashboard.py")

show_sidebar()

history = trading_client.get_portfolio_history()

equity_df = pd.DataFrame({
    "timestamp": history.timestamp,
    "equity": history.equity
})

equity_df["timestamp"] = pd.to_datetime(
    equity_df["timestamp"],
    unit="s"
)

st.line_chart(
    equity_df.set_index("timestamp")["equity"]
)

fig = px.line(
    equity_df,
    x="timestamp",
    y="equity"
)

st.plotly_chart(fig, use_container_width=True)