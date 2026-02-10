import logging

from config import WATCHLIST
from scanner import scan_stock
from utils import is_market_open


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.INFO,
        # format="%(asctime)s %(levelname)s %(name)s - %(message)s",
        format="%(name)s - %(message)s",
    )

    # if not is_market_open():
    #     print("🕒 Market is closed. Scanner not running.")
    #     return

    logger.info("🔍 Starting Pattern Hunter...")
    for ticker in WATCHLIST:
        try:
            result = scan_stock(ticker)
            if result:
                logger.info("✅ Signal found for %s: %s", ticker, result["signals"])
            else:
                logger.info("❌ No signal for %s", ticker)
        except Exception as e:
            logger.exception("❌ Error processing %s", ticker)

if __name__ == "__main__":
    main()
