import API
import requests
import json
import pprint

url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

headers = {
    'X-CMC_PRO_API_KEY': API.Api_key,
    "accepts": "application/json",
}

params = {
    "id": "4172",
    "convert": "USD"
}

response = requests.get(url, params=params, headers=headers).json()
price = 0

price = response["data"]["4172"]["quote"]["USD"]["price"]

print(float(price))


