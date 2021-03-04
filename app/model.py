from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    firstName = db.Column(db.String(150), nullable=False)
    lastName = db.Column(db.String(150), nullable=False)
    phoneNum = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    address = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(150), nullable=False)
    state = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    
    def __init__(self,username,firstName,lastName,phoneNum,email,address,city,state,password):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNum = phoneNum
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.password = generate_password_hash(password)