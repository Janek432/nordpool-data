import requests
import json
from datetime import datetime, timezone

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
start = f"{today}T00:00:00Z"
end   = f"{today}T23:59:59Z"

url = f"https://dashboard.elering.ee/api/nps/price?start={start}&end={end}"

print("Requesting:", url)

with requests.get(url, stream=True, timeout=20) as r:
    r.raise_for_status()

    raw = ""
    for chunk in r.iter_content(chunk_size=16384):
        if chunk:
            raw += chunk.decode("utf-8")

print("Downloaded length:", len(raw))

data = json.loads(raw)

with open("data/today_prices.json", "w") as f:
    json.dump(data, f, indent=2)

print("Saved today_prices.json")
