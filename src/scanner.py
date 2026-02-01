from datetime import datetime
from patterns import apply_indicators, detect_pattern
from config import DATA_FETCH_INTERVAL, DATA_FETCH_PERIOD
from data.yfinance_provider import YFinanceProvider


provider = YFinanceProvider()


def scan_stock(ticker: str):
    df = provider.fetch_ohlc(
        ticker=ticker,
        interval=DATA_FETCH_INTERVAL,
        period=DATA_FETCH_PERIOD
    )

    if df.empty or len(df) < 50:
        print(f"No data fetched for {ticker}")
        return None

    df = apply_indicators(df)
    signals = detect_pattern(df)

    if not signals:
        print(f"No signals generated for {ticker}")
        return None
    
    return {
        "ticker": ticker,
        "signals": signals,
        "price": round(df["Close"].iloc[-1], 2),
        "last_updated": datetime.now().strftime("%H:%M:%S")
    }
