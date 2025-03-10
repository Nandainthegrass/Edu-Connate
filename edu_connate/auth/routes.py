from flask import Flask
from edu_connate.admin import admin_bp

@admin_bp.route("/student")
def user_login():
    pass

@admin_bp.route("/admin")
def admin_login():
    pass
