from patterns.bullish_engulfing import (
    find_bullish_engulfing,
    plot_all_bullish_engulfing
)

def detect_pattern(df, ticker):
    signals = []

    engulf_indices = find_bullish_engulfing(df)

    if not engulf_indices:
        return []

    img_path = plot_all_bullish_engulfing(df, engulf_indices, ticker)

    for i in engulf_indices:
        signals.append({
            "pattern": "Bullish Engulfing",
            "time": df.index[i],
            "price": float(df["Close"].iloc[i]),
            "chart": img_path
        })

    return signals
