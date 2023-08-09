import streamlit as st
from app.utils import page_setup, load_leap_data

st.set_page_config(page_title="Landry LEAP", layout="wide")
page_setup()

st.title("Landry LEAP Results")

landry = load_leap_data("Landry")

st.write('Hello World!')