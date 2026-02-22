from flask import Blueprint, request, jsonify
from services.rag_service import generate_rag_response

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message required"}), 400

    response = generate_rag_response(user_message)

    return jsonify({"response": response})