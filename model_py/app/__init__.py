from flask import Flask
from app.routes import prediction_app

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(prediction_app)
    return app
