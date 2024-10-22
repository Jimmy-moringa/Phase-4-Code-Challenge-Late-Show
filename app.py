from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models import Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Routes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict())
    return jsonify({'error': 'Episode not found'}), 404

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400

if __name__ == '__main__':
    app.run(debug=True)
