from app import db
from flask_sqlalchemy import SQLAlchemy



class Photo(db.Model):
    __tablename__ = 'class_photos'

    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(80), unique = True, nullable=False)
    img_filename =  db.Column(db.String())
    week = db.Column(db.Integer)

    
    def __init__(self, img_filename, week): #do not initialize pri key
        self.img_filename = img_filename
        self.week = week

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
        'id': self.id,
        'img_filename': self.img_filename,
        'week': self.week     
        }

class Student(db.Model):
    __tablename__ = 'student_photos'

    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(80), unique = True, nullable=False)
    student_photo = db.Column(db.String())
    student_section = db.Column(db.String())
    encodings = db.Column(db.String())

    def __init__(self, student_id, student_name, student_photo, student_section, encodings): #do not initialize pri key
        self.student_id = student_id
        self.student_name = student_name
        self.student_photo = student_photo
        self.student_section = student_section
        self.encodings = encodings

    def __repr__(self):
        return '<id {}>'.format(self.student_id)
    
    def serialize(self):
        return {
        'id': self.student_id,
        'name': self.student_name,
        'photo': self.student_photo,
        'encodings': self.encodings,
        'section': self.student_section
        }

def add_image(image_dict):
    new_image = Photo(name=image_dict['name'], img_filename=image_dict['img_filename'], img_data=image_dict['img_data'])
    db.session.add(new_image)
    db.session.commit()    