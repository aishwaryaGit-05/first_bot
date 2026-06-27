from auth.auth import supabase
import streamlit as st

def login(email, password):
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    if response.user:
        st.session_state["user"] = response.user
        st.session_state["logged_in"] = True
        st.success("Login successful")
        st.switch_page("./pages/watchlist.py")
    else:
        st.error("Invalid credentials")