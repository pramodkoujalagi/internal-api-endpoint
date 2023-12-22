import csv
from app import db
from app.database import Card

def populate_database():
    with open('data/Delivered.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            card = Card(id=row['ID'], card_id=row['Card ID'], user_contact=row['User contact'],
                        timestamp=row['Timestamp'], comment=row['Comment'])
            db.session.add(card)

        db.session.commit()
