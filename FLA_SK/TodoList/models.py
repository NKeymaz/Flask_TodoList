from TodoList import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(130), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(230), nullable=False, unique=True)
    city = db.Column(db.String(80), nullable=False,default='IRAN')