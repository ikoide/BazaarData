import os

from flask import Flask

from bazaar.extensions import (
    db,
    scheduler
)

def create_app(config_filename="flask.cfg"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    initialize_extensions(app)
    register_blueprints(app)

    return app

def initialize_extensions(app):
    db.init_app(app)

    return None

def register_blueprints(app):
    from bazaar.api.api import api

    app.register_blueprint(api)

    return None

def register_scheduler(app):
    from bazaar.hypixel.tasks import updateItems

    if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        scheduler.init_app(app)
        scheduler.start()

    return None
