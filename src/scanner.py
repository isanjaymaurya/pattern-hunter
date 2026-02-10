import logging
from datetime import datetime, time
import pytz

from config import DATA_FETCH_INTERVAL, DATA_FETCH_PERIOD
from data.yfinance_provider import YFinanceProvider
from detect_pattern import detect_pattern

provider = YFinanceProvider()
logger = logging.getLogger(__name__)


# ================= MARKET HOURS CHECK =================
def is_market_open():
    india_tz = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india_tz).time()

    market_open = time(9, 15)
    market_close = time(15, 30)

    return market_open <= now <= market_close


# ================= MAIN SCANNER =================
def scan_stock(ticker: str):
    try:
        # Fetch data
        df = provider.fetch_ohlc(
            ticker=ticker,
            interval=DATA_FETCH_INTERVAL,
            period=DATA_FETCH_PERIOD
        )

        if df is None or df.empty or len(df) < 50:
            logger.info("No data fetched for %s", ticker)
            return None

        # Ensure only today’s data
        today = datetime.now().date()
        df = df[df.index.date == today]

        if df.empty:
            logger.info("No intraday data for today: %s", ticker)
            return None

        # Detect patterns
        signals = detect_pattern(df, ticker)

        if not signals:
            logger.info("No signals generated for %s", ticker)
            return None

        return {
            "ticker": ticker,
            "signals": signals,
            "price": round(float(df["Close"].iloc[-1]), 2),
            "last_updated": datetime.now().strftime("%H:%M:%S")
        }

    except Exception as e:
        logger.exception("❌ Error scanning %s: %s", ticker, str(e))
        return None
