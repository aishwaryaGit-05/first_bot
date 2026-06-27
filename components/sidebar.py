import streamlit as st

def show_sidebar():

    with st.sidebar:

        st.title("Trading Bot")

        st.page_link("pages/orders.py", label="Orders")

        st.page_link("pages/portfolio.py", label="Portfolio")

        st.page_link("pages/performance.py", label="Performance")

        st.page_link("pages/positions.py", label="Positions")

        st.page_link("pages/watchlist.py", label="Watchlist")

        st.divider()

        if st.button("Logout"):
            st.session_state.clear()
            st.switch_page("dashboard.py")