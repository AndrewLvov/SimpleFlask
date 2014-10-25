from app import db


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.Text())


class Car(db.Model):
    __tablename__ = "cars"
    name = db.Column(db.Text, primary_key=True)
    price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    owner = db.relationship('Person', backref=db.backref('cars'))


