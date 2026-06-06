from main import run_trades
import streamlit as st
# import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from config import API_KEY, SECRET_KEY, BASE_URL
import pandas as pd
import time
from strategy_bot import data_indicators, get_strategy_data
from data_collector import get_price_data
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import QueryOrderStatus
# from streamlit_option_menu import option_menu


API_KEY = API_KEY
SECRET_KEY = SECRET_KEY
BASE_URL = BASE_URL


st.set_page_config(
    page_title="Trading Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Trading Dashboard")

st.write("Select a page from the sidebar.")

# page = st.sidebar.radio(
#     "Navigate",
#     [
#         "Portfolio",
#         "Positions",
#         "Orders",
#         "Performance",
#         "Market Watchlist"
#     ]
# )

#  old script
col1, col2, col3 = st.columns(3)

run_bot = col1.button("Run Bot")
load_price = col2.button("Load price data")

if run_bot:

    # trading logic here
    try:
        # api = TradingClient.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")
        api = TradingClient(API_KEY, SECRET_KEY, paper=True)
        st.success("Connected to Alpaca")
    except Exception as e:
        st.error(e)

    # if st.button("Run strategy now"):
        print("Running strategy...")
        trade_history = run_trades()
        st.dataframe(pd.DataFrame(trade_history))

    account = api.get_account()

    st.subheader("Account Info")
    st.write("Equity:", account.equity)
    st.write("Buying Power:", account.buying_power)

    # rsiValue = improved_strategy()
    # st.subheader("RSI Values")
    # st.write(rsiValue[['Close', 'RSI']].tail(10))fs
    # st.line_chart(rsiValue['RSI'])

    request_params = GetOrdersRequest(
    status=QueryOrderStatus.OPEN,
    limit=20
   )      

    positions = api.get_all_positions()

    st.subheader("Open Positions")

    for position in positions:
        st.write("Symbol:", position.symbol, "Quantity:", position.qty, "Current Price:", position.current_price)

        orders = api.get_orders(filter=request_params)
        data = [
            {"Symbol": order.symbol, "Side": order.side, "Qty": order.qty, "Status": order.status}
            for order in orders
        ]

        if data:
            st.dataframe(pd.DataFrame(data))
        else:
            st.info("No open orders found")
    
    # before button
    # data_for_chart = get_price_data("AAPL")
    # stock_data = data_indicators(data_for_chart)

    # st.line_chart(stock_data[['short_ma', 'long_ma', 'ma200']])
    # st.line_chart(stock_data['rsi'])

    # st.subheader("Trade History")
    # st.subheader("Open Positions with P&L")


    total_pl = sum(float(p.unrealized_pl) for p in positions)

    # st.subheader("Total Unrealized P&L")

    # if total_pl > 0:
    #     st.success(f"Profit: ${total_pl:.2f}")
    # else:
    #     st.error(f"Loss: ${total_pl:.2f}")

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

    # st.bar_chart(pl_data)

    time.sleep(60)
    st.rerun()
    st.write("Bot Running")

 # enclosed inside a button due to deployment
if load_price:
    data_for_chart = get_price_data("AAPL")
    stock_data = data_indicators(data_for_chart)

    st.subheader("AAPL Strategy Data")
    # st.write(stock_data[['Close', 'RSI']].tail(10))
    st.line_chart(stock_data[['short_ma', 'long_ma', 'ma200']])
    st.line_chart(stock_data['rsi'])

# # from main import get_main_data


