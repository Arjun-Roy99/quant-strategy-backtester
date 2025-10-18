import streamlit as st
import matplotlib.pyplot as plt
import datetime
import pandas as pd
from utils.data_loader import load_data
from utils.strategies import golden_cross, rsi_mean_reversion
from utils.backtester import backtest


st.set_page_config(page_title = "Quant Strategy Backtester", layout = "wide")

st.title("Quant Strategy Backtester")

ticker = st.selectbox("Select Stock", ["RELIANCE", "TCS", "INFY", "ICICIBANK", "SBIN"])
strategy = st.selectbox("Select Strategy", ["Golden Cross", "RSI Mean Reversion"])
start_date = st.date_input("Select the start date", datetime.date(2025,1,1))
end_date = st.date_input("Select the end date", datetime.date.today())



if st.button("Run Backtest"):

    if start_date < end_date:
        df = load_data(ticker, start_date, end_date) #Load Stock Data
        if strategy == "Golden Cross":
            df = golden_cross(df)
        elif strategy == "RSI Mean Reversion":
            df = rsi_mean_reversion(df)

        df, metrics = backtest(df)

        #Plot Performance of Strategy
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(df.index, df["Cumulative_Strategy"], label="Strategy")
        ax.plot(df.index, df["Cumulative_Benchmark"], label="Benchmark (Buy & Hold)")
        ax.legend()
        st.pyplot(fig)

        # Metrics
        st.subheader("📊 Performance Metrics")
        st.write(metrics)

    else:
        st.info("Please enter valid start and end dates")

st.markdown("---")
st.caption("Built by AR99 | Data powered by Yahoo Finance")



