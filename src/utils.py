import pandas as pd
from datetime import datetime, time

from config import IST, MARKET_CLOSE_TIME, MARKET_OPEN_TIME

def _to_float(value):
    """
    Safely convert pandas value to float.
    Returns None if not possible.
    """
    try:
        if isinstance(value, pd.Series):
            value = value.iloc[0]
        return float(value)
    except Exception:
        return None


def is_market_open():
    """
    Check if the current time is within market hours (9:30 AM to 3:30 PM IST).
    """
    now = datetime.now(IST).time()
    return MARKET_OPEN_TIME <= now <= MARKET_CLOSE_TIME
