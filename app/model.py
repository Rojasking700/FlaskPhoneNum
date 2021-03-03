from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150), nullable=False, unique=True)
    lastName = db.Column(db.String(150), nullable=False, unique=True)
    phoneNum = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    address = db.Column(db.String(150), nullable=False, unique=True)
    city = db.Column(db.String(150), nullable=False, unique=True)
    state = db.Column(db.String(150), nullable=False, unique=True)
    
    def __init__(self,firstName,lastName,phoneNum,email,address,city,state):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNum = phoneNum
        self.email = email
        self.address = address
        self.city = city
        self.state = state