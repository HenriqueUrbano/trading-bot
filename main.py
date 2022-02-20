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

avgprices = [0.00012,1.034,332917,23096.90,13.7241,5.313,240.81,0.0001727,3599,1283.9]
profit = ""
counter = 0
for i in symbols:
    x = urllib.request.urlopen(api + "?symbol=" + i).read()
    json_data = json.loads(x)
    result = float(json_data['price']) - avgprices[counter]
    if result > 0:
        profit = "Lucro!"
    else:
        profit = "Prejuízo!"
    print(json_data['symbol'] + ' Price: ' + json_data['price'])
    print("Resultado = " + profit)
    counter = counter + 1
