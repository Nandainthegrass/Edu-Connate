from flask import Flask
from edu_connate.routes.home import home_bp


#register all home routes here
def register_routes(app):
    app.register_blueprint(home_bp)