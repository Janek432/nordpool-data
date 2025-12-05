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

# --- Filtreeri ainult EE hind ---
ee_entries = []

for entry in raw["data"]:
    if entry["area"] == "EE":
        # Teisenda timestamp UNIX sekunditeks
        ts = int(datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00")).timestamp())

        ee_entries.append({
            "timestamp": ts,
            "price": entry["price"]
        })

# --- Lõplik struktuur ESP8266 jaoks ---
final = {
    "success": True,
    "data": {
        "ee": ee_entries
    }
}

# Salvesta õigesse faili
with open("data/today_prices.json", "w") as f:
    json.dump(final, f, indent=2)

print("Kirjutatud today_prices.json", len(ee_entries), "rea hinnad")
