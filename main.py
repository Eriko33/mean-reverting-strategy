from data.loader import load_pair_data
from strategy.mean_reversion import MeanRevertingModel
from backtest.backtester import run_backtest
from report.performance import report_performance

def main():
    prices_a, prices_b = load_pair_data('AAPL', 'MSFT')
    model = MeanRevertingModel(prices_a, prices_b)
    z_scores = model.fit()
    signals = model.generate_signals()
    result = run_backtest(prices_a, prices_b, signals)
    report_performance(result)

if __name__ == "__main__":
    main()
