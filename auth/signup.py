from supabase import create_client  # type: ignore
import streamlit as st
from auth.auth import supabase

def signup(email, password):

    response = supabase.auth.sign_up({
        "email": email,
        "password": password
    })
    
    existing = (
        supabase.table("profiles")
        .select("id")
        .eq("id", response.user.id)
        .execute()
    )

    if not existing.data:
        supabase.table("profiles").insert({
        "id": response.user.id,
        "email": response.user.email
        }).execute()
    return response