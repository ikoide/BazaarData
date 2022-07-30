from flask import Blueprint, render_template

from bazaar.hypixel.models import Item

main = Blueprint("main", __name__)

@main.route("/")
def home():
    items = Item.objects()

    return render_template("index.html", items=items)
