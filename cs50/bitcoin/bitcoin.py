import requests
import sys

if len(sys.argv) != 2:
    sys.exit("How many bitcoins?")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("bad request")

n = int(sys.argv[1])

o = response.json()

price = o["bpi"]["USD"]["rate_float"]
cost = n * price

print(f"{n} BTC = ${cost:,.2f}")
