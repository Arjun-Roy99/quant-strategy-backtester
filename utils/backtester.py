import numpy as np

def backtest(df):
    df["Strategy_Return"] = df["Signal"].shift(1) * df["Return"]
    df["Cumulative_Strategy"] = (1 + df["Strategy_Return"]).cumprod()
    df["Cumulative_Benchmark"] = (1 + df["Return"]).cumprod()

    sharpe = np.sqrt(252) * df["Strategy_Return"].mean() / df["Strategy_Return"].std()

    max_dd = (df["Cumulative_Strategy"] / df["Cumulative_Strategy"].cummax() - 1).min()

    metrics = {
        "CAGR": (df["Cumulative_Strategy"].iloc[-1]) ** (252 / len(df)) - 1,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": max_dd
    }
    return df, metrics