import requests
import json

url = "https://www.nordpoolgroup.com/api/marketdata/page/10?currency=EUR"
response = requests.get(url)
data = response.json()

# Otsime Eesti hinnad
ee_prices = {}
for row in data["data"]["Rows"]:
    if row["Name"] == "EE":
        for i, col in enumerate(row["Columns"]):
            val = col["Value"].replace(",", ".")
            ee_prices[i] = float(val)

# Salvestame faili
with open("data/today_prices.json", "w") as f:
    json.dump(ee_prices, f, indent=2)
