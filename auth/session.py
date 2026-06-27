import streamlit as st

def is_logged_in():

    return "user" in st.session_state

def logout():

    if "user" in st.session_state:
        del st.session_state["user"]