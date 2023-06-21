from flask import Flask, render_template, request, make_response, jsonify, redirect, url_for,session
import requests
from flask_oidc import OpenIDConnect
from functools import wraps
from requests.exceptions import ConnectionError, HTTPError


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


@app.route('/allowedop')
def get_allowed_main_operations():
     try:
            return redirect('http://172.25.1.60:4001/home')
     except ConnectionError:
            return make_response('auth login service is down\n', 404)
     except HTTPError:
            return make_response('Invalid input from auth login\n', 400)
@app.route('/allowed')
def allowed_main_operations():
    x = request.args.get('x') 
    return x
    

@app.route('/main')
def main(): 
       return render_template('index.html')


@app.route('/view')
def view():
       return render_template('view.html')

@app.route('/show')
def show():
       return render_template('data.html')

@app.route('/login')
def login():
       return "render_template('login.html')"


def create_app():
    return app


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4002)
