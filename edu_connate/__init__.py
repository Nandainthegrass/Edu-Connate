from flask import Flask
from edu_connate.models import db
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from edu_connate.admin import admin_bp
from edu_connate.user import user_bp
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    migrate = Migrate(app, db)

    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("Tables created")

    return app