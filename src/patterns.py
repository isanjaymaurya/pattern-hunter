import logging

import pandas as pd
import pandas_ta as ta

from config import RSI_OVERBOUGHT, RSI_OVERSOLD


logger = logging.getLogger(__name__)


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


def apply_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply technical indicators to the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing OHLC data.

    Returns:
        pd.DataFrame: DataFrame with added technical indicators.
    """
    df = df.copy()

    try:
        df["rsi"] = ta.rsi(df["Close"], length=14)
        df["ema20"] = ta.ema(df["Close"], length=20)
        df["ema50"] = ta.ema(df["Close"], length=50)
        df["vol_ma"] = ta.sma(df["Volume"], length=20)
    except Exception as e:
        logger.exception("⚠️ Indicator calculation failed")

    return df


def detect_pattern(df: pd.DataFrame) -> list:
    signals = []

    try:
        if df is None or df.empty or len(df) < 50:
            return signals

        last = df.iloc[-1]
        prev = df.iloc[-2]

        rsi = _to_float(last.get("rsi"))
        ema20 = _to_float(last.get("ema20"))
        ema50 = _to_float(last.get("ema50"))
        prev_ema20 = _to_float(prev.get("ema20"))
        prev_ema50 = _to_float(prev.get("ema50"))
        volume = _to_float(last.get("Volume"))
        vol_ma = _to_float(last.get("vol_ma"))

        # RSI Oversold
        if rsi is not None and rsi < RSI_OVERSOLD:
            signals.append("RSI Oversold")

        # RSI Overbought
        if rsi is not None and rsi > RSI_OVERBOUGHT:
            signals.append("RSI Overbought")

        # EMA Bullish Crossover
        if (
            prev_ema20 is not None 
            and prev_ema50 is not None 
            and ema20 is not None 
            and ema50 is not None
            and prev_ema20 < prev_ema50
            and ema20 > ema50
        ):
            signals.append("EMA20 Bullish Crossover")

        # EMA Bearish Crossover
        if (
            prev_ema20 is not None
            and prev_ema50 is not None
            and ema20 is not None
            and ema50 is not None
            and prev_ema20 > prev_ema50
            and ema20 < ema50
        ):
            signals.append("EMA20 Bearish Crossover")

        # Volume Spike
        if (
            volume is not None 
            and vol_ma is not None 
            and volume > 1.5 * vol_ma
        ):
            signals.append("Volume Spike")

        logger.info(
            "RSI=%s, EMA20=%s, EMA50=%s, Volume=%s, VolMA=%s",
            rsi,
            ema20,
            ema50,
            volume,
            vol_ma,
        )

        return signals
    except Exception as e:
        logger.exception("⚠️ Pattern detection failed")
        
    return signals
