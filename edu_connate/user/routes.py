from flask import Flask, flash, render_template, request
from edu_connate.user import user_bp
from edu_connate.models import db
from edu_connate.models.course import Course
from edu_connate.models.user import User


@user_bp.route("/", methods=["GET", "POST"])
def create_user_controller():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        selected_courses = request.form.getlist("courses")
        role = "student"

        new_student = User(name=name, email=email, password=password, role = role)

        for course_id in selected_courses:
            course = Course.query.get(course_id)
            if course:
                new_student.courses.append(course)

        db.session.add(new_student)
        db.session.commit()

        flash("Student created successfully!", "success")
        return
    
    courses = Course.query.all()
    return render_template("create_student.html", courses = courses)