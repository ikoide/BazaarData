from datetime import datetime

from bazaar.app import db

class ItemHistoric(db.EmbeddedDocument):
    sellPrice = db.FloatField()
    sellVolume = db.IntField()
    sellMovingWeek = db.IntField()
    sellOrders = db.IntField()
    buyPrice = db.FloatField()
    buyVolume = db.IntField()
    buyMovingWeek = db.IntField()
    buyOrders = db.IntField()
    datetime = db.DateTimeField(default=datetime.utcnow())

class Item(db.Document):
    name = db.StringField()
    history = db.ListField(db.EmbeddedDocumentField("ItemHistoric"))
