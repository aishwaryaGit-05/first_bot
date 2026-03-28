import streamlit as st
import alpaca_trade_api as tradeapi
from config import API_KEY, SECRET_KEY, BASE_URL
import pandas as pd
import time


API_KEY = API_KEY
SECRET_KEY = SECRET_KEY
BASE_URL = BASE_URL

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

st.title("Trading Bot Dashboard")

account = api.get_account()

st.subheader("Account Info")
st.write("Equity:", account.equity)
st.write("Buying Power:", account.buying_power)

positions = api.list_positions()

st.subheader("Open Positions")

for position in positions:
    st.write(position.symbol, position.qty, position.current_price)

data = []

orders = api.list_orders(status='closed', limit=20)

for order in orders:
    data.append({
        "Symbol": order.symbol,
        "Side": order.side,
        "Qty": order.qty,
        "Status": order.status,
        "Entry Price": float(position.avg_entry_price),
        "Current Price": float(position.current_price),
        "Unrealized P&L": float(position.unrealized_pl)
    })

df = pd.DataFrame(data)
st.dataframe(df)
# st.subheader("Trade History")
st.subheader("Open Positions with P&L")


total_pl = sum(float(p.unrealized_pl) for p in positions)

st.subheader("Total Unrealized P&L")

if total_pl > 0:
    st.success(f"Profit: ${total_pl:.2f}")
else:
    st.error(f"Loss: ${total_pl:.2f}")
    
equity = float(account.equity)
last_equity = float(account.last_equity)

daily_pl = equity - last_equity

st.subheader("Daily P&L")

if daily_pl > 0:
    st.success(f"Today's Profit: ${daily_pl:.2f}")
else:
    st.error(f"Today's Loss: ${daily_pl:.2f}")

pl_data = pd.DataFrame({
    "P&L": [total_pl]
})

st.bar_chart(pl_data)

time.sleep(10)
st.rerun()
