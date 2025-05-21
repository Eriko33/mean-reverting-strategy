import pandas as pd
from strategy.mean_reversion import MeanRevertingModel

def test_model_fit():
    # Create dummy price data
    price_a = pd.Series(range(100, 200))
    price_b = pd.Series(range(101, 201))

    model = MeanRevertingModel(price_a, price_b)
    zscore = model.fit()

    assert len(zscore) == len(price_a)
    assert zscore.isna().sum() == 0
