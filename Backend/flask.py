from flask import Flask, jsonify
#from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#CORS(app)

# Configure your MySQL database connection string
app.config['SQLACHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://JOSH:Secured@19@localhost/Nebula'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Define a simple model representing a Student
class Student (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    score = db.Column(db.Float)

# Sample route to fetch student data from the database
@app.route('/api/get_students', methods=['GET'])
def get_students():
    try:
        #Query all students from the database
        students = Student.query.all()

        # Convert the list of Student objects to a list of dictionaries
        student_data = [{'id': student.id, 'name': student.name, 'score': student.score} for student in students]

        return jsonify({'success': True, 'data': student_data})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    