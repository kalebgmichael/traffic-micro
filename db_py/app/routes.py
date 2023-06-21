from flask import request, jsonify
from app import app
from app.models import VehicleRecord
from app.controllers import get_data


@app.route('/getdata')
def get_data_route():
    return get_data()


@app.route('/home')
def login1():
    return "Welcome Guest! <a href='/login'>Login</a>"
