from flask import Flask, jsonify, redirect, url_for, session,render_template,request
from flask_oidc import OpenIDConnect
from functools import wraps
from werkzeug.datastructures import Headers
import requests
from requests.exceptions import ConnectionError, HTTPError
from urllib.parse import urlencode


app = Flask(__name__)
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

# @app.route('/home')
# def home():
#     if oidc.user_loggedin:
#         "Welcome  ! <a href='/logout'>Login</a>"
#     else:
#         return "Welcome Guest not allowed ! <a href='/login'>Login</a>"

@app.route('/login')
@oidc.require_login
def login():
    if oidc.user_loggedin:
        session['access_token'] = oidc.get_access_token()
        gateway_url = 'http://172.25.1.60:4000'  # Replace with the URL of your API gateway
        redirect_url = f"{gateway_url}/main/view1"
        params = {'access_token': session['access_token']}
        redirect_url_with_params = f"{redirect_url}?{urlencode(params)}"
        return redirect(redirect_url_with_params)
       

@app.route('/logout')
def logout():
    oidc.logout()
    session.pop('access_token', None)
    session.pop('username', None)
    return redirect(oidc.client_secrets['issuer'] + '/protocol/openid-connect/logout')

@app.route('/home')
@oidc.require_login
def login1():
    if oidc.user_loggedin:
        username = oidc.user_getfield('username')
        x = 'success'
        return x
    else:
        return "Welcome Guest! <a href='/login'>Login</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)



