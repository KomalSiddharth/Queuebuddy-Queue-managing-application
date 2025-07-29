from flask import Blueprint, request, jsonify
from queue_logic import join_queue, get_queue, next_customer

# Create a Blueprint for the queue
queue_bp = Blueprint('queue_bp', __name__)

# Route to join the queue (expects JSON data with 'name')
@queue_bp.route('/join', methods=['POST'])
def join():
    data = request.get_json()
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    position = join_queue(name)
    return jsonify({
        "message": f"{name} joined the queue",
        "position": position
    })

# Route to get the current queue
@queue_bp.route('/queue', methods=['GET'])
def view_queue():
    return jsonify({
        "queue": get_queue()
    })

# Route to serve the next customer
@queue_bp.route('/next', methods=['POST'])
def next_user():
    next_person = next_customer()
    
    if next_person:
        return jsonify({
            "message": f"{next_person} can be served now"
        })
    
    return jsonify({
        "message": "Queue is empty"
    })
