import requests

def get_crypto_price(crypto="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data[crypto]["usd"]
        print(f"Current price of {crypto.capitalize()}: ${price}")
    else:
        print("Error fetching data")
if __name__ == "__main__":
    crypto_name = input("Enter the crypto currency name (eg. bitcoin, ethereum):").lower()
    get_crypto_price(crypto_name)
    