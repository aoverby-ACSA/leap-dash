import streamlit as st
from app.utils import page_setup

st.set_page_config(page_title="ACSA LEAP Dashboard", layout="wide")

page_setup()

st.title("ACSA LEAP Dashboard")
st.header("Welcome to the ACSA LEAP Dashboard")
st.markdown("##### Click on a topic to expand each help section below")

with st.expander(label="**How to Use**",):
    st.subheader("How to Use")
    st.markdown("Use the sidebar to select which page to view. Each schools' pages are grouped in their own sections on the sidebar underneath the name of the school. Once on a page, there may also tabs located at the top of the page leading to different data views. You will find data filters on a page's sidebar. You can hide the sidebar by using the 'X' located on the top right of the sidebar. You can always bring the sidebar back by clicking the '>' which will appear on the top left of the page after the sidebar has been hidden. The hamburger menu on the top right contains helpful commands that will allow you to change theme settings, print a page or record a screencast.")

with st.expander(label="**Contents Summary**"):
    st.subheader("Contents Summary")
    st.markdown("Here you will find a brief description of each page and the contents therein.")
    
with st.expander(label="**Questions? Feedback?**"):
    st.subheader("Questions? Feedback?")
    st.markdown("Please send any questions and/or feedback to Anton Overby at antonio.overby@theacsa.org.")