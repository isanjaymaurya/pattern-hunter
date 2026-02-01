from abc import ABC, abstractmethod

class MarketDataProvider(ABC):

    @abstractmethod
    def fetch_ohlc(self, ticker: str, interval: str, period: str):
        """Fetch OHLC data for a given ticker, interval, and period."""
        pass
