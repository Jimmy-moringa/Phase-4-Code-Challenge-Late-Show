from app import db
from models import Episode, Guest, Appearance

def seed_data():
    # Create sample episodes
    episode1 = Episode(date="1/11/99", number=1)
    episode2 = Episode(date="1/12/99", number=2)

    # Create sample guests
    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="comedian")

    # Create sample appearances
    appearance1 = Appearance(rating=5, episode=episode1, guest=guest1)
    appearance2 = Appearance(rating=4, episode=episode2, guest=guest2)

    db.session.add_all([episode1, episode2, guest1, guest2, appearance1, appearance2])
    db.session.commit()

if __name__ == '__main__':
    seed_data()
