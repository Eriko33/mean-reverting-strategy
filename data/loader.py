import pandas as pd
import numpy as np

def load_pair_data(symbol_a, symbol_b):
    # Dummy price series (replace with actual data loading)
    np.random.seed(0)
    price_a = pd.Series(100 + np.cumsum(np.random.normal(0, 1, 100)))
    price_b = pd.Series(100 + np.cumsum(np.random.normal(0, 1, 100)))
    return price_a, price_b
