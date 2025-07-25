import requests
import json
import os

Gold_API_url = "https://www.goldapi.io/api/XAU/USD"
headers = {"x-access-token": os.getenv("GOLDAPI_KEY")}
response = requests.get(Gold_API_url, headers=headers)
output = response.json()

with open("Gold_price.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=1)
