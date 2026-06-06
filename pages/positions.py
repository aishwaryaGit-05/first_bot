from alpaca.trading.client import TradingClient
from config import API_KEY, SECRET_KEY, BASE_URL
import streamlit as st
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
import pandas as pd

positions = trading_client.get_all_positions()

data = []

for p in positions:

    data.append({
        "Symbol": p.symbol,
        "Qty": float(p.qty),
        "Avg Price": float(p.avg_entry_price),
        "Market Value": float(p.market_value),
        "P&L": float(p.unrealized_pl),
        "P&L %": float(p.unrealized_plpc) * 100
    })

df = pd.DataFrame(data)

st.subheader("Open Positions")
st.dataframe(df, use_container_width=True)