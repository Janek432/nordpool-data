import requests
import json

url = "https://www.nordpoolgroup.com/api/marketdata/page/10?currency=EUR"
response = requests.get(url)

# Kontrollime, mis me saime
print("HTTP status:", response.status_code)
print("Content starts with:", response.text[:100])  # ainult esimesed 100 märki

# Proovime alles siis JSON-i
try:
    data = response.json()
except Exception as e:
    print("JSON parse error:", e)
    exit(1)
