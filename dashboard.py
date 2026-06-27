import streamlit as st
from auth.login import login
from auth.signup import signup

# API_KEY = API_KEY
# SECRET_KEY = SECRET_KEY
# BASE_URL = BASE_URL

# if "user" not in st.session_state:
#     st.error("Please login first")
#     st.stop()

#     st.set_page_config(
#     page_title="Trading Dashboard",
#     page_icon="📈",
#     layout="wide"
#     )

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

if not st.session_state.get("logged_in"):
    st.set_page_config(
        page_title="Trading Bot",
        initial_sidebar_state="collapsed"
    )

tab1, tab2 = st.tabs(["Login", "Signup"])

with tab1:

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        response = login(email, password)

        st.session_state["user"] = response.user

        st.rerun()

with tab2:

    email = st.text_input("Signup Email")
    password = st.text_input("Signup Password", type="password")

    if st.button("Signup"):
        try:
            signup(email, password)
            st.success("Check your email")
        except Exception as e:
            st.error(f"Error occurred: {e}")



# # from main import get_main_data


