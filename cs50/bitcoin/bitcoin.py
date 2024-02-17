import sys

import requests

if len(sys.argv) != 2:
    sys.exit("How many bitcoins?")

api_string = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(api_string)
except requests.RequestException:
    sys.exit("bad request")

n = int(sys.argv[1])

o = response.json()

price = o["bpi"]["USD"]["rate_float"]
cost = n * price

print(f"{n} BTC = ${cost:,.2f}")
