# Renko Trading Bot Demo

This repository is a **demo trading bot** showing how to fetch real-time market data from Binance, build **Renko charts**, and generate buy/sell signals.

> ⚠️ Educational/demo only — not financial advice. No execution on real funds.

## Features
- Live price fetcher from Binance API (REST/WebSocket)
- Renko chart builder (configurable brick size)
- Signal generation (buy/sell)
- Backtesting on historical OHLCV
- Telegram alerts integration (demo)
- Modular, clean code (Python 3.10+)

## Stack
- Python (pandas, numpy)
- `python-binance` for market data
- `TA-Lib` for indicators
- Matplotlib (for charting Renko bricks)
- Pytest for testing

## Quick Start
```bash
git clone https://github.com/<you>/renko-trading-bot-demo.git
cd renko-trading-bot-demo
pip install -r requirements.txt

# Run backtest
python src/backtest.py --symbol BTCUSDT --interval 1h --brick-size 100

# Run live signal fetcher
python src/live_trading.py --symbol BTCUSDT --brick-size 50
```

## Example Renko Chart
![renko](./notebooks/sample_renko.png)

## License
MIT
