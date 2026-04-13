"""Fetch and display the current price of gold."""

import json
import urllib.request


def get_gold_price():
    """Fetch the current gold price in USD per ounce from the GoldAPI.io free endpoint."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=tether-gold&vs_currencies=usd"
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode())
    return data["tether-gold"]["usd"]


if __name__ == "__main__":
    try:
        price = get_gold_price()
        print(f"Gold current price: ${price:,.2f} USD per ounce")
    except Exception as e:
        print(f"Failed to fetch gold price: {e}")
