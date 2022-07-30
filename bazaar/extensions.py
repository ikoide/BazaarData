from flask_mongoengine import MongoEngine
from flask_apscheduler import APScheduler

db = MongoEngine()
scheduler = APScheduler()
