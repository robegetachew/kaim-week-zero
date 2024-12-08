import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def add_custom_css():
    st.markdown(
        """
        <style>
        .css-1aumxhk {
            background-color: #FF6052; /* Sidebar color */
        }
        .stApp {
            background-color: #f0f2f5; /* Main background color */
        }
        h1, h2, h3, h4 {
            color: #1f77b4; /* Header color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_analysis_togo():
    add_custom_css()  # Add custom CSS
    st.write('Togo')
    url = '../data/togo-dapaong_qc.csv'
    df = pd.read_csv(url)

    st.title('Solar Radiation of Togo Dashboard')
    st.write(df.head())

    # Plot GHI over time
    st.subheader('GHI over Time')
    fig, ax = plt.subplots(figsize=(12, 6))
    df.plot(x='Timestamp', y='GHI', ax=ax)
    st.pyplot(fig)

    # Plot histogram of GHI
    st.subheader('Histogram of GHI')
    fig, ax = plt.subplots(figsize=(10, 6))
    df['GHI'].hist(ax=ax, bins=20)
    st.pyplot(fig)