from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': '12345',
    'AUTH_SERVICE_URL': 'http://172.25.1.60:4001'
})



def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'access_token' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('home')) 

    return decorated


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://stats:stats@172.25.1.60/stats_db"
db = SQLAlchemy(app)



from app import routes
