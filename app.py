from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import db
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///late_show.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Set up Flask-Migrate

from models import Episode, Guest, Appearance
from routes import *
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    # Validate rating
    if rating < 1 or rating > 5:
        return jsonify({"errors": ["Rating must be between 1 and 5"]}), 400

    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify(appearance.to_dict()), 201
if __name__ == "__main__":
    app.run(debug=True)
