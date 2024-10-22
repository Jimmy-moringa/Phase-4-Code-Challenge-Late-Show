from app import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    number = db.Column(db.Integer)
    appearances = db.relationship('Appearance', backref='episode', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'appearances': [appearance.to_dict() for appearance in self.appearances]
        }

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    occupation = db.Column(db.String(100))
    appearances = db.relationship('Appearance', backref='guest', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)

    def __init__(self, rating, episode_id, guest_id):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self.rating = rating
        self.episode_id = episode_id
        self.guest_id = guest_id

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id,
            'guest': self.guest.to_dict(),
            'episode': self.episode.to_dict()
        }
