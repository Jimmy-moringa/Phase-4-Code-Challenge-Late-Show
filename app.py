from flask import flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///late_show.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

from models import Episode, Gest, Appearance
from routes import *

if __name__ == '__main__':
    db.create_all()  # Create the database tables if not already exists
    app.run(debug=True)