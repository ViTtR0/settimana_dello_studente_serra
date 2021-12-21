from models.db import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False, unique=True) # Password sha256(64)
    email = db.Column(db.String(80), nullable=True, unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password