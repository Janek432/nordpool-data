import requests
import json
from datetime import datetime

# Kuupäev täna
today = datetime.utcnow().strftime("%Y-%m-%d")
start = f"{today}T00:00:00Z"
end   = f"{today}T23:59:59Z"

url = f"https://dashboard.elering.ee/api/nps/price?start={start}&end={end}"

resp = requests.get(url, timeout=10)
print("HTTP status:", resp.status_code)
print("Vastus algusest:", resp.text[:200])

raw = resp.json()

# --- VÕTA OTSE EE ANDMED ---
ee_only = raw["data"]["ee"]

# --- PANE NEED ESP8266 FORMAATI ---
final = {
    "success": True,
    "data": {
        "ee": ee_only
    }
}

# Salvesta GitHubi
with open("data/today_prices.json", "w") as f:
    json.dump(final, f, indent=2)

print("Salvestatud EE hinnad:", len(ee_only), "kirjet")
