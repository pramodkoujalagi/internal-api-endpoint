from app import db

class Card(db.Model):
    id = db.Column(db.String, primary_key=True)
    card_id = db.Column(db.String, nullable=False)
    user_contact = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
