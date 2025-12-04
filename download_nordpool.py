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
print("Vastus algusest:", resp.text[:100])

data = resp.json()

# Salvesta GitHubi kasutamiseks JSON faili
with open("data/today_prices.json", "w") as f:
    json.dump(data, f, indent=2)
