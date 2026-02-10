from datetime import time
import pytz

IST = pytz.timezone("Asia/Kolkata")

MARKET_OPEN_TIME = time(9, 30)
MARKET_CLOSE_TIME = time(15, 30)

WATCHLIST = [
    "TCS.NS",
    "RELIANCE.NS",
    "HDFCBANK.NS",
    "INFY.NS",
    # "ICICIBANK.NS",
    # "KOTAKBANK.NS",
    # "SBIN.NS",
    # "HINDUNILVR.NS",
    # "BAJFINANCE.NS",
    # "AXISBANK.NS",
    # "ECLERX.NS",
    "TIJARIA.NS"
]

DATA_PROVIDER = "yfinance"  # Options: 'yfinance' etc.
DATA_FETCH_INTERVAL = "5m"  # Options: '1d', '1h', '15m', etc.
DATA_FETCH_PERIOD = "1d"  # Options: '1mo', '3mo', '6mo', '1y', etc.

RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
