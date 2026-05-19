from main import run_trades
import streamlit as st
import alpaca_trade_api as tradeapi
from config import API_KEY, SECRET_KEY, BASE_URL
import pandas as pd
import time
from strategy_bot import data_indicators, get_strategy_data
from data_collector import get_price_data

API_KEY = API_KEY
SECRET_KEY = SECRET_KEY
BASE_URL = BASE_URL

st.title("Trading Bot")

if st.button("Run Bot"):

    # trading logic here
    try:
        api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")
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

    positions = api.list_positions()

    st.subheader("Open Positions")

    for position in positions:
        st.write("Symbol:", position.symbol, "Quantity:", position.qty, "Current Price:", position.current_price)

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

    data_for_chart = get_price_data("AAPL")
    stock_data = data_indicators(data_for_chart)

    st.line_chart(stock_data[['short_ma', 'long_ma', 'ma200']])
    st.line_chart(stock_data['rsi'])

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

# # from main import get_main_data


