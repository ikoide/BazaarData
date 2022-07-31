import requests

from bazaar.extensions import scheduler
from bazaar.hypixel.models import Item, ItemHistoric

@scheduler.task("cron", id="updateItems", minute="*", misfire_grace_time=900)
def updateItems():
    r = requests.get("https://api.hypixel.net/skyblock/bazaar")
    json = r.json()
    products = json["products"]

    for item in products:
        item = products[item]["quick_status"]
        item_db = Item.objects(name=item["productId"]).first()

        if not item_db:
            item_db = Item(name=item["productId"])

        itemHistoric = ItemHistoric(
            sellPrice = item["sellPrice"],
            sellVolume = item["sellVolume"],
            sellMovingWeek = item["sellMovingWeek"],
            sellOrders = item["sellOrders"],
            buyPrice = item["buyPrice"],
            buyVolume = item["buyVolume"],
            buyMovingWeek = item["buyMovingWeek"],
            buyOrders = item["buyOrders"]
        )

        item_db.history.append(itemHistoric)
        item_db.save()

    print(f"Updated Items: {len(products)}")
