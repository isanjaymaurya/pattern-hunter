from datetime import datetime
import os
import mplfinance as mpf


def find_bullish_engulfing(df):
    indices = []

    for i in range(1, len(df)):
        prev = df.iloc[i - 1]
        curr = df.iloc[i]

        if (
            prev["Close"] < prev["Open"] and
            curr["Close"] > curr["Open"] and
            curr["Open"] < prev["Close"] and
            curr["Close"] > prev["Open"]
        ):
            indices.append(i)

    return indices


# ================================
# Plot ALL bullish engulfing
# ================================
def plot_all_bullish_engulfing(df, indices, ticker):
    if not indices:
        return None

    os.makedirs("charts", exist_ok=True)

    lines = []

    for i in indices:
        prev_i = i - 1
        curr_i = i

        low = min(df["Low"].iloc[prev_i], df["Low"].iloc[curr_i])
        high = max(df["High"].iloc[prev_i], df["High"].iloc[curr_i])

        t1 = df.index[prev_i]
        t2 = df.index[curr_i]

        # rectangle using 4 lines
        lines.extend([
            [(t1, low), (t2, low)],
            [(t1, high), (t2, high)],
            [(t1, low), (t1, high)],
            [(t2, low), (t2, high)],
        ])

    filename = f"charts/{datetime.now().strftime('%Y-%m-%d')}_{ticker}_BullishEngulfing.png"

    mpf.plot(
        df,
        type="candle",
        style="yahoo",
        volume=False,
        title=f"{ticker} Bullish Engulfing Patterns",
        alines=dict(
            alines=lines,
            colors="green",
            linewidths=1.8
        ),
        savefig=dict(fname=filename, dpi=150, bbox_inches="tight")
    )

    return filename
