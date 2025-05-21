def report_performance(result):
    pnl = result['pnl'].dropna()
    total_return = pnl.sum()
    sharpe_ratio = pnl.mean() / pnl.std() * (252 ** 0.5)
    max_drawdown = (pnl.cumsum() - pnl.cumsum().cummax()).min()
    print(f"Total PnL: {total_return:.2f}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Max Drawdown: {max_drawdown:.2f}")
