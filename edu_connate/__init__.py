from flask import Flask
from edu_connate.models import db
import os
from dotenv import load_dotenv
from edu_connate.routes import register_routes

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_routes(app)

    db.init_app(app)

    return app