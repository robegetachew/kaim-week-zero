import streamlit as st
from benin_dashboard import show_analysis_benin
from togo_dashboard import show_analysis_togo
from sierraleone import show_analysis_sierra

# Sidebar selection for navigation
page = st.sidebar.selectbox('Explore or Predict', ["Benin", "Togo", "Sierraleone"])

if page == "Benin":
    show_analysis_benin()
elif page == "Togo":
    show_analysis_togo()
elif page == "Sierraleone":
    show_analysis_sierra()