from edu_connate.models import db

student_courses = db.Table(
    'student_courses',
    db.Column('student_id', db.Integer, db.ForeignKey('student_id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course_id'), primary_key=True)
)