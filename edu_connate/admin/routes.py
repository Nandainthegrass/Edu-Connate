from flask import render_template
from edu_connate.admin import admin_bp

@admin_bp.route("/")
def admin_dashboard():
    return render_template("home.html")