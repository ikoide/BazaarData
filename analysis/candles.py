import time
import requests

import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

from ohlc import genOHLC

def getData(item_name):
    r = requests.get(f"https://bazaar.sewer.fail/api/v1/item/{item_name}")
    #r = requests.get(f"http://localhost:9000/api/v1/item/{item_name}")
    data = r.json()

    return data

def graphData(item_name, timeframe):
    json = getData(item_name)
    data = {}
    data["dates"], data["prices"], data["volumes"] = json["datetimes"], json["buyPrice"], json["buyVolume"]
    data = pd.DataFrame(genOHLC(timeframe, data))
    data.index = pd.to_datetime(data.dates)

    print(data)

    mpf.plot(data, type="candle", style="yahoo", mav=(10, 20), volume=True, title=f"\n{item_name.replace('_', ' ')}")

def browseItems():
    while True:
        item = input("Item Name: ")
        timeframe = input("Timeframe: ")
        graphData(item, int(timeframe))

if __name__ == "__main__":
    #browseItems()
    graphData("ENCHANTED_GLISTERING_MELON", 5)
