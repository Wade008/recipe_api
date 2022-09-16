from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# objects
db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.app_config")

    # Initialise
    db.init_app(app)

    return app


