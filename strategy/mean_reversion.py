import numpy as np
import statsmodels.api as sm

class MeanRevertingModel:
    def __init__(self, prices_a, prices_b):
        self.prices_a = prices_a
        self.prices_b = prices_b
        self.model = None
        self.zscore = None

    def fit(self):
        X = sm.add_constant(self.prices_b)
        model = sm.OLS(self.prices_a, X).fit()
        self.model = model
        spread = self.prices_a - model.predict(X)
        self.zscore = (spread - spread.mean()) / spread.std()
        return self.zscore

    def generate_signals(self, entry_z=1.5, exit_z=0.5):
        signals = []
        for z in self.zscore:
            if z > entry_z:
                signals.append(-1)
            elif z < -entry_z:
                signals.append(1)
            elif abs(z) < exit_z:
                signals.append(0)
            else:
                signals.append(None)
        return signals
