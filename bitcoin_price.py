"""Fetch and display the current price of Bitcoin."""

import json
import urllib.request


def get_bitcoin_price():
    """Fetch the current Bitcoin price in USD from the CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode())
    return data["bitcoin"]["usd"]


if __name__ == "__main__":
    try:
        price = get_bitcoin_price()
        print(f"Bitcoin current price: ${price:,.2f} USD")
    except Exception as e:
        print(f"Failed to fetch Bitcoin price: {e}")
