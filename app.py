from app import app
from flask import jsonify, request
from app import app, db
from app.database import Card
from app.models import populate_database

# Uncomment the next line for the first run to populate the database
populate_database()

@app.route('/get_card_status', methods=['GET'])
def get_card_status():
    user_input = request.args.get('user_input')
    if not user_input:
        return jsonify({'error': 'Please provide a user phone number or card ID'}), 400

    # Assuming user_input is either phone number or card ID
    card = Card.query.filter((Card.user_contact == user_input) | (Card.card_id == user_input)).first()

    if not card:
        return jsonify({'error': 'Card not found'}), 404

    return jsonify({
        'card_id': card.card_id,
        'status': card.comment,
        'timestamp': card.timestamp
    })

if __name__ == '__main__':
    app.run(debug=True)
