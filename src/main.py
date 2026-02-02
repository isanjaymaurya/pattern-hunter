import logging

from config import WATCHLIST
from scanner import scan_stock


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    logger.info("🔍 Starting Pattern Hunter...")

    for ticker in WATCHLIST:
        try:
            result = scan_stock(ticker)
            if result:
                logger.info("📊 SIGNAL FOUND")
                logger.info("Stock   : %s", result["ticker"])
                logger.info("Price   : ₹%s", result["price"])
                logger.info("Time    : %s", result["last_updated"])
                logger.info("Signals : %s", ", ".join(result["signals"]))
                logger.info("%s", "-" * 35)
        except Exception as e:
            logger.exception("❌ Error processing %s", ticker)

if __name__ == "__main__":
    main()
