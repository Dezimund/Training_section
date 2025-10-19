from db import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    date_add = db.Column(db.DateTime, nullable=False)
    date_finish = db.Column(db.DateTime, nullable=True)
