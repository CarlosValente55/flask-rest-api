from flask import Flask
from flask_bcrypt import Bcrypt
from . import model,controller,service
from .config import config_by_name
from flask_pymongo import PyMongo
from main.controller.workout_controller import workout,notification

flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    flask_bcrypt.init_app(app)

    __register_blueprints(app)
    return app



def __register_blueprints(app):
    app.register_blueprint(workout)
    app.register_blueprint(notification)
    
