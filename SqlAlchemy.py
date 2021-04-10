from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\shrinidhi.mahishi\SQLLite\Test.db'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

class student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    addr = db.Column(db.String(100))
    pin = db.Column(db.String(100))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def display():
    return render_template('show.html', students = student.query.all())        

@app.route('/new', methods = ['POST', 'GET'])
def new():
    if request.method == 'POST':
        dict = request.form
        if not dict['name'] or not dict['city'] or not dict['addr'] or not dict['pin']:
            flash('Please enter all details', 'error')
        else:
            stud = student(dict['name'], dict['city'], dict['addr'], dict['pin'])
            db.session.add(stud)
            db.session.commit()
            flash('Record inserted successfully')
            return redirect(url_for('display'))
    return render_template('new.html')       

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

