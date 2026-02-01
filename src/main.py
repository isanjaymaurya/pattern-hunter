from config import WATCHLIST
from scanner import scan_stock


def main():
    print("🔍 Starting Pattern Hunter...\n")

    for ticker in WATCHLIST:
        try:
            result = scan_stock(ticker)
            if result:
                print("📊 SIGNAL FOUND")
                print(f"Stock   : {result['ticker']}")
                print(f"Price   : ₹{result['price']}")
                print(f"Time    : {result['last_updated']}")
                print(f"Signals : {', '.join(result['signals'])}")
                print("-" * 35)
        except Exception as e:
            print(f"❌ Error processing {ticker}: {e}")

if __name__ == "__main__":
    main()
