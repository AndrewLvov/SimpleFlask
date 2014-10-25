
import os
from flask import Flask, render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy

from random import randrange

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.db')
app.debug = True
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    from models import Person
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


@app.route('/persons/')
def persons():
    from models import Person
    people = Person.query.all()
    return render_template('persons.html', people=people)


@app.route('/persons/<person_id>/')
def person_detail(person_id):
    from models import Person
    p = Person.query.get(person_id)
    return render_template('person_detail.html', person=p)


@app.route('/persons/add/', methods=['GET', 'POST'])
def person_add():
    from models import Person

    if request.method == 'POST':
        name = request.form['name']
        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        db.session.refresh(person)
        return redirect('/persons/{}/'.format(person.id))
    else:
        return render_template('person_add.html')


if __name__ == '__main__':
    app.run(port=80)
