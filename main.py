from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# objects
db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.app_config")

    # Initialise objects
    db.init_app(app)

    # register cli commands blueprint
    from commands import db_commands
    app.register_blueprint(db_commands)

    return app
