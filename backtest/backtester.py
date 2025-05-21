import pandas as pd

def run_backtest(prices_a, prices_b, signals):
    positions = pd.Series(signals).fillna(method='ffill').fillna(0)
    pnl = positions.shift(1) * (prices_a - prices_a.shift(1) - (prices_b - prices_b.shift(1)))
    result = pd.DataFrame({
        "position": positions,
        "pnl": pnl
    })
    return result
