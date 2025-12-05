import requests
import json
from datetime import datetime, timezone

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
start = f"{today}T00:00:00Z"
end   = f"{today}T23:59:59Z"

url = f"https://dashboard.elering.ee/api/nps/price?start={start}&end={end}"

resp = requests.get(url, timeout=10)
data = resp.json()

ee_list = []

# convert €/MWh → s/kWh
for entry in data["data"]["ee"]:
    price_eur_mwh = entry["price"]
    price_s_kwh = price_eur_mwh / 10.0  # because 100 €/MWh = 10 s/kWh

    ee_list.append({
        "timestamp": entry["timestamp"],
        "price": round(price_s_kwh, 4)
    })

with open("data/today_prices.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data/ee_today.json", "w") as f:
    json.dump(ee_list, f, indent=2)

print("Converted and saved prices:", len(ee_list))
