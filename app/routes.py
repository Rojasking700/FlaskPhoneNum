from app import app
from flask import render_template, request
# from app.forms import UserInfoForm, PostForm

@app.route('/')
@app.route('/index')
def hello_world():
    title = 'Index'
    return render_template('index.html', title=title)

@app.route('/RegisterPhoneNum')
def RegisterPhoneNum():
    title = 'Register Phone Number'
    return render_template('registerPhone.html',title=title)