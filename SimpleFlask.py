
import os
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

from random import randrange

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.db')
# app.debug = True
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())


class Car(db.Model):
    __tablename__ = "cars"
    name = db.Column(db.Text, primary_key=True)
    price = db.Column(db.Integer)
    owner = db.Column(db.Integer, db.ForeignKey('persons.id'))
    owner_p = db.relationship('Person', backref=db.backref('cars'))


@app.route('/')
def hello_world():
    people = Person.query.all()
    return render_template('index.html', name="Кот Васька",
                           people=people)


@app.route('/sum/', methods=['GET', 'POST'])
def sum_handler():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        return render_template('sum.html', a=a, b=b, total=int(a) + int(b))
    else:
        return render_template('sum.html')


if __name__ == '__main__':
    app.run(port=80)
