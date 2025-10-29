import requests
import time
from datetime import datetime

API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_price(crypto="bitcoin"):
    params = {
        "ids": crypto,
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        price = data[crypto]["usd"]
        change = data[crypto].get("usd_24h_change", 0)
        return price, change
    else:
        return None, None


def main():
    print("\n🚀 Live Crypto Price Tracker")
    print("Type 'exit' to stop.\n")

    while True:
        crypto = input("Enter cryptocurrency (e.g., bitcoin, ethereum): ").lower()

        if crypto == "exit":
            break

        price, change = get_crypto_price(crypto)

        if price:
            arrow = "📈" if change >= 0 else "📉"
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] {crypto.capitalize()}: ${price:.2f} {arrow}")
            print(f"24h Change: {change:.2f}%\n")
        else:
            print("❌ Unable to fetch data. Check crypto name.\n")

        time.sleep(1)

if __name__ == "__main__":
    main()
