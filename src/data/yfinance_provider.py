import yfinance as yf
import pandas as pd

from data.base import MarketDataProvider

class YFinanceProvider(MarketDataProvider):

    def fetch_ohlc(self, ticker: str, interval: str, period: str) -> pd.DataFrame:
        """
        Fetch OHLC data for a given ticker, interval, and period using yfinance.

        Args:
            ticker (str): The stock ticker symbol.
            interval (str): The data interval (e.g., '1d', '1h').
            period (str): The data period (e.g., '1mo', '1y').
        """
        df = yf.download(
            ticker,
            interval=interval,
            period=period,
            progress=False # Displays a progress bar during ticker downloads when set to True; disables progress bar if logging is in DEBUG mode to avoid interference with log messages.
        )

        # Fix yfinance multi-index columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        if df is None or df.empty:
            return pd.DataFrame()
        
        df.dropna(inplace=True)
        
        return df
