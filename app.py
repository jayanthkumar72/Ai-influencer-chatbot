import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template
from config import Config

# Import Blueprints
from routes.chat_routes import chat_bp
from routes.pricing_routes import pricing_bp
from routes.brief_routes import brief_bp
from routes.health_routes import health_bp

from services.rag_service import generate_rag_response

# Import database
from database.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register Blueprints
    app.register_blueprint(chat_bp)
    app.register_blueprint(pricing_bp)
    app.register_blueprint(brief_bp)
    app.register_blueprint(health_bp)

    #  Add Homepage Route
    @app.route("/")
    def home():
        return render_template("chat.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
