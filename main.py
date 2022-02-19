import json
import requests
import urllib.request

api = "https://api.binance.com/api/v3/ticker/price"

symbols = ["SHIBBRL",
           "DOGEBRL",
           "BTCBRL",
           "ETHBRL",
           "C98BRL",
           "XRPBRL",
           "LINKBRL",
           "MANABRL",
           "BNBBRL",
           "LTCBRL"]

prices = []

for i in symbols:
    x = urllib.request.urlopen(api + "?symbol=" + i).read()
    print(x)
