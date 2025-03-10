from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from edu_connate.auth import routes