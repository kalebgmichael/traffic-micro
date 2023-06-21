import requests
from flask import Flask, render_template, request, make_response, jsonify, redirect, url_for,session
from datetime import datetime
from requests.exceptions import ConnectionError, HTTPError
from urls import *
from flask_oidc import OpenIDConnect
from functools import wraps
from werkzeug.datastructures import Headers
from urllib.parse import parse_qs

ALLOWED_PREDICT_OPS = ['predict_file', 'predict']
ALLOWED_MAIN_OPS = ['main','view','login','show']
ALLOWED_DB_OPS = ['getdata','upload']
ALLOWED_AUTH_OPS= ['login','logout','home','main/view']

app = Flask(__name__, instance_relative_config=True)

app.config.update({
    'SECRET_KEY': '12345',
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_COOKIE_SECURE': False,
    'OIDC_CALLBACK_ROUTE': '/oidc/callback'
})

oidc = OpenIDConnect(app)


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if oidc.user_loggedin:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return decorated


      
# app.before_request(before_request_handler)

@app.route('/auth/<op>')
def auth(op):

    if op not in ALLOWED_AUTH_OPS:
        return make_response('Invalid operation from auth\n', 404)
    if op == "login":
        try:
            return redirect('http://172.25.1.60:4001/login')
        except ConnectionError:
            return make_response('auth login service is down\n', 404)
        except HTTPError:
            return make_response('Invalid input from auth login\n', 400)
    elif op == "logout":
        try:
            session.pop('access_token', None)
            session['access_token'] = None
            session.clear()
            return redirect('http://172.25.1.60:4001/logout')
        except ConnectionError:
            return make_response('auth logout service is down\n', 404)
        except HTTPError:
            return make_response('Invalid input from auth logout\n', 400)
    

    elif op == "home":
        try:
            return redirect('http://172.25.1.60:4001/home')
        except ConnectionError:
            return make_response('auth logout service is down\n', 404)
        except HTTPError:
            return make_response('Invalid input from auth logout\n', 400)


@app.route('/model/<op>', methods=["GET"])
@oidc.require_login
def predict(op):
        date = request.args.get('date')
        if op not in ALLOWED_PREDICT_OPS:
            return make_response('Invalid operation from model\n', 404)
        try:
            # headers = {'Authorization': f'Bearer {session["access_token"]}'}
            x = requests.get(MODEL_URL + f'/{op}?date={date}')
            #x.raise_for_status()
            return jsonify(x.json())
        except ConnectionError:
            return make_response('Model service is down from gateway\n', 404)
        except HTTPError:
            return make_response('Invalid input from model service\n', 400)
   


@app.route('/main/<op>')
@oidc.require_login
def main(op):
        if op not in ALLOWED_MAIN_OPS:
            return make_response('Invalid operation from main\n', 404)
        if op == "main":
            try:
                # headers = {'Authorization': f'Bearer {session["access_token"]}'}
                x = requests.get(MAIN_URL + f'/{op}')
                return x.text
            except ConnectionError:
                return make_response('Main index service is down\n', 404)
            except HTTPError:
                return make_response('Invalid input from main index\n', 400)
        elif op == "view":
            try:
                x = requests.get(MAIN_URL + f'/{op}')
                return x.text
            except ConnectionError:
                return make_response('Main view service is down\n', 404)
            except HTTPError:
                return make_response('Invalid input from main view\n', 400)
        
        elif op == "show":
            try:
                x = requests.get(MAIN_URL + f'/{op}')
                return x.text
            except ConnectionError:
                return make_response('Main view service is down\n', 404)
            except HTTPError:
                return make_response('Invalid input from main view\n', 400)
    
    

        elif op == "login":
            try:
                return redirect(f"{AUTH_URL}/{op}")
            except ConnectionError:
                return make_response('auth login service is down\n', 404)
            except HTTPError:
                return make_response('Invalid input from main view\n',400)
  
    


@app.route('/main/view1')
def main_view_proxy():
        return redirect('http://172.25.1.60:4000/main/view')
      

@app.route('/data/<op>')
@oidc.require_login
def stats_service(op):
        date = request.args.get('date')
        if op not in ALLOWED_DB_OPS:
            return make_response('Invalid operation from getdata\n', 404)
        if op == "getdata":
            try:
                # headers = {'Authorization': f'Bearer {session["access_token"]}'}
                x = requests.get(DB_URL + f'/{op}?date={date}')
                x.raise_for_status()
                return jsonify(x.json())
            except ConnectionError:
                return make_response('db-service is down\n', 404)
            except HTTPError:
                return make_response('Invalid input from db-service\n', 400)
        
        elif op == "upload":
            try:
                # headers = {'Authorization': f'Bearer {session["access_token"]}'}
                x = requests.post(DB_URL + f'/{op}')
                x.raise_for_status()
                return jsonify(x.json())
            except ConnectionError:
                return make_response('db-service is down\n', 404)
            except HTTPError:
                return make_response('Invalid input from db-service\n', 400)


@app.route('/home')
@login_required
def login1():
    if 'access_token' in session:
        # username = oidc.user_getfield('username')  # Get the username from the user's claims
        return f"welcome guest <a href='/logout'>Logout</a>"
    else:
        return "Welcome Guest! <a href='/login'>Login</a>"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000,debug=True)
