from flask import Flask
from flask_bootstrap import Bootstrap
from config import configs

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(configs[config_name])