# auth.py

from supabase import create_client  # type: ignore
import streamlit as st
# from config import SUPABASE_URL, SUPABASE_KEY

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(
    url,
    key
)