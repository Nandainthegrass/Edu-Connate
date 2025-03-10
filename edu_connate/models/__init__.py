from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from edu_connate.models.user import User
from edu_connate.models.course import Course
from edu_connate.models.associations import student_courses