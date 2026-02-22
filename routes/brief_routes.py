from flask import Blueprint, request, jsonify
from services.brief_generator import generate_campaign_brief

brief_bp = Blueprint("brief", __name__)

@brief_bp.route("/generate-brief", methods=["POST"])
def generate_brief():
    data = request.get_json()

    brief = generate_campaign_brief(data)

    return jsonify({"brief": brief})