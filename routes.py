from flask import jsonify, request
from app import app, db  # Import db here
from models import Episode, Appearance, Guest

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        episode_data = episode.to_dict()
        episode_data['appearances'] = [
            appearance.to_dict() for appearance in Appearance.query.filter_by(episode_id=id)
        ]
        return jsonify(episode_data)
    return jsonify({"error": "Episode not found"}), 404

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
