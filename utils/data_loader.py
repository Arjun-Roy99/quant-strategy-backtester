import yfinance as yf
import pandas as pd
import streamlit as st

@st.cache_data(ttl = 3600)
def load_data(ticker, start_date, end_date):
    df = yf.download(ticker + ".NS", start=start_date, end = end_date)
    df.dropna(inplace=True)
    df["Return"] = df["Close"].pct_change()
    return df
