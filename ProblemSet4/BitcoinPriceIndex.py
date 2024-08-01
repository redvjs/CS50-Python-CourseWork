import requests
import sys
import json


if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")
else:
    x = sys.argv[1]

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    cost = o["bpi"]["USD"]["rate_float"]
    price = float(cost) * float(sys.argv[1])
    print(f"${price:,.4f}")
except requests.RequestException:
    print("Request not available")
