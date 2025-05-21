# Mean Reverting Strategy Framework

A modular mean-reverting trading strategy implemented in Python. Includes:
- Cointegration-based signal generation
- Backtesting engine
- PnL and performance report
- Real-time integration stubs
- Execution layer for trading simulation

## Structure

- `data/`: Data loading and streaming
- `strategy/`: Signal generation and mean-reverting logic
- `backtest/`: Backtest engine
- `execution/`: Trading simulator and real execution
- `report/`: PnL and performance evaluation
- `config/`: Configuration files
- `cpp/`: Reserved for C++ optimization (e.g., pybind11)

## Run

```bash
pip install -r requirements.txt
python main.py
```

