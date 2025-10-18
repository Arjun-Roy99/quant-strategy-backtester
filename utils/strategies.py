
import pandas as pd
import pandas_ta as ta

def golden_cross(df):
    df["EMA5"] = df["Close"].ewm(span = 5).mean()
    df["EMA9"] = df["Close"].ewm(span = 9).mean()
    df["EMA14"] = df["Close"].ewm(span = 14).mean()
    df["Signal"] = 0
    df.loc[(df["EMA5"] > df["EMA9"]) & (df["EMA9"] > df["EMA14"]), "Signal"] = 1
    df.loc[(df["EMA5"] < df["EMA9"]) & (df["EMA9"] < df["EMA14"]), "Signal"] = -1
    return df

def rsi_mean_reversion(df, lower = 30, upper = 70):
    df["RSI"] = ta.rsi(df["Close"], length = 14)
    df["Signal"] = 0
    df.loc[df["RSI"] < lower, "Signal"] = 1 #buy
    df.loc[df["RSI"] > upper, "Signal"] = -1 #sell
    return df
    
    