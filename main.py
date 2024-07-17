import os, streamlit as st
import pandas as pd
from polygon import RESTClient

st.subheader("Polygon+Streamlit Demo App")
symbol = st.text_input("Enter a stock symbol", "AAPL")

with st.sidebar:
    #Get your Polygon API key from the dashboard. 
    #In a real app you want to store this as a secret in your .env
    polygon_api_key = st.text_input("Polygon API Key", type="password")
	# Authenticate with the Polygon API
    client = RESTClient(polygon_api_key)
    col1, col2, col3 = st.columns(3)