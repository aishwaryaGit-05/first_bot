
from alpaca.trading.client import TradingClient
from config import API_KEY, SECRET_KEY, BASE_URL
import streamlit as st
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
import pandas as pd
from components.sidebar import show_sidebar
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import QueryOrderStatus

if not st.session_state.get("logged_in"):
    st.switch_page("dashboard.py")

show_sidebar()


request = GetOrdersRequest(
    status=QueryOrderStatus.ALL,
    limit=50
)

orders = trading_client.get_orders(
    filter=request
)

order_data = []

for order in orders:

    order_data.append({
        "Symbol": order.symbol,
        "Side": order.side,
        "Qty": order.qty,
        "Status": order.status,
        "Type": order.order_type
    })

st.dataframe(pd.DataFrame(order_data))