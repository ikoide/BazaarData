import json

from flask import Blueprint, Response

from bazaar.hypixel.models import Item

api = Blueprint("api", __name__)

@api.route("/api/v1/item/<string:item_name>")
def item(item_name):
    item = Item.objects(name=item_name).first()

    sellPrice = []
    sellVolume = []
    sellMovingWeek = []
    sellOrders = []
    buyPrice = []
    buyVolume = []
    buyMovingWeek = []
    buyOrders = []
    datetimes = []

    for historicItem in item.history:
        sellPrice.append(historicItem.sellPrice)
        sellVolume.append(historicItem.sellVolume)
        sellMovingWeek.append(historicItem.sellMovingWeek)
        sellOrders.append(historicItem.sellOrders)
        buyPrice.append(historicItem.buyPrice)
        buyVolume.append(historicItem.buyVolume)
        buyMovingWeek.append(historicItem.buyMovingWeek)
        buyOrders.append(historicItem.buyOrders)
        datetimes.append(str(historicItem.datetime))

    data = {
        "name": item.name,
        "sellPrice": sellPrice,
        "sellVolume": sellVolume,
        "sellMovingWeek": sellMovingWeek,
        "sellOrders": sellOrders,
        "buyPrice": buyPrice,
        "buyVolume": buyVolume,
        "buyMovingWeek": buyMovingWeek,
        "buyOrders": buyOrders,
        "datetimes": datetimes
    }

    return Response(json.dumps(data), mimetype="application/json")
