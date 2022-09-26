from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# objects
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():

    app = Flask(__name__)

    app.config.from_object("config.app_config")

    # Initialise objects
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # register cli commands blueprint
    from commands import db_commands
    app.register_blueprint(db_commands)

    # register all controllers
    from controllers import registerable_contollers
    for controller in registerable_contollers:
        app.register_blueprint(controller)

    return app
