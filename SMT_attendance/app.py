# Step 01: import necessary libraries/modules
from flask import Flask, jsonify, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from PIL import Image, ImageDraw, ImageFont
from ast import literal_eval
import numpy as np
import face_recognition
import os



app = Flask(__name__, template_folder='templates', static_folder='static')

#configurations
UPLOAD_FOLDER = "./app_storage"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
student_jpg = "./student_photo"
app.config['students'] = student_jpg
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kinmeng:password@localhost:5432/attendance_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from models import Photo, Student, add_image

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/uploader/', methods=['POST','GET'])
def uploader():
	if request.method == 'GET':
   		return render_template('upload.html')
	if request.method == 'POST':
		os.makedirs('app_storage', exist_ok=True)
		photo_objects = request.files.getlist('file')
		week_number = request.form.get('week_number')
		for photo in photo_objects:
			new_image = Photo(img_filename=photo.filename, week=week_number)
			db.session.add(new_image)
			db.session.commit()    
			print("image saved")
			photo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(photo.filename)))
			return redirect(url_for('processPhoto'))

# @app.route('/uploader/', methods=['POST','GET'])
# def upload_photo():
# 	if request.method == 'POST':
# 		os.makedirs('app_storage', exist_ok=True)
# 		photo_objects = request.files.getlist('file')
# 		for photo in photo_objects:
# 			photo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(photo.filename)))
# 			# print(photo.filename)
# 			# new_image = Photo(name=7, img_filename=photo.filename, img_data=photo.read())
# 			# db.session.add(new_image)
# 			# db.session.commit()    
			
# 			print(photo)
# 			photo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(photo.filename)))
# 			return "you uploaded successfully"
# 	if request.method == 'GET':
# 		returned_photos = Photo.query.all()
# 		return jsonify([m.serialize() for m in returned_photos])

@app.route('/student/', methods=['POST', 'GET'])
def student():
	if request.method == 'POST':
		student_name = request.form.get('student_name')
		student_id = request.form.get('student_id')
		student_section = request.form.get('student_section')
		student_photo = request.files['file']
		try:
			filepath = os.path.join(app.config['students'], secure_filename(student_photo.filename))
			student_photo.save(filepath)
			picture_of_student = face_recognition.load_image_file(filepath)
			face_encoding = face_recognition.face_encodings(picture_of_student)[0]
			face_encoding = face_encoding.tolist()
			face_encoding = str(face_encoding)
	
			new_student = Student(student_name= student_name, student_photo=student_photo.filename, student_id=student_id, student_section=student_section, encodings=face_encoding) #based on init function
			db.session.add(new_student)
			db.session.commit()
			
			return jsonify('{} was created'.format(new_student))
		except Exception as e:
			return (str(e))
	if request.method == 'GET':
		return render_template('student_reg.html')



@app.route('/processPhoto/', methods=['GET'])
def processPhoto():
	if request.method == 'GET':
		att_list = []
		found_students =[]
		students_encoding=[]
		
		class_photos = Photo.query.filter_by(week=1)
		for image in class_photos:
			image = image.serialize()
			path = './app_storage/'+ image['img_filename']
			class_photo = face_recognition.load_image_file(path)
			face_locations_class = face_recognition.face_locations(class_photo)
			face_encodings_class = face_recognition.face_encodings(class_photo, face_locations_class)

			

		returned_students = Student.query.filter_by(student_section='G1')	
		for student in returned_students:
			student = student.serialize()
			face_encoding_student = student['encodings']
			face_encoding_student = literal_eval(face_encoding_student)
			face_encoding_student = np.asarray(face_encoding_student)
			if student['name'] not in found_students:
				results = face_recognition.compare_faces(face_encodings_class, face_encoding_student)
				if results[0] == True:
					att_list.append({'name': student['name'], 'attendance':'present'})
					found_students.append(student['name'])
				else: 
					att_list.append({'name': student['name'], 'attendance':'absent'})
					found_students.append(student['name'])
		return render_template('displayer.html', att_list=att_list)








if __name__ == '__main__':
   app.run(debug = True)