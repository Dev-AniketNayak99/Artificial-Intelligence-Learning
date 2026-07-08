import streamlit as st
from config import *

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

st.title(APP_NAME)

st.write("Welcome to the AI Resume Analyzer.")