from flask import Blueprint, request, jsonify
from services.pricing_engine import estimate_price

pricing_bp = Blueprint("pricing", __name__)

@pricing_bp.route("/pricing", methods=["POST"])
def pricing():
    data = request.get_json()

    followers = int(data.get("followers", 0))
    engagement_rate = float(data.get("engagement_rate", 0))
    niche = data.get("niche", "lifestyle")

    price = estimate_price(followers, engagement_rate, niche)

    return jsonify({"suggested_price": price})