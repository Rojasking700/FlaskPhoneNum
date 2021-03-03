from app import app
from flask import render_template, request
from app.forms import RegisterPhoneForm

@app.route('/')
@app.route('/index')
def hello_world():
    title = 'Index'
    return render_template('index.html', title=title)

@app.route('/RegisterPhoneNum', methods=['GET','POST'])
def RegisterPhoneNum():
    title = 'Register Phone Number'
    regPhone = RegisterPhoneForm()
    if request.method == 'POST' and regPhone.validate:
        firstName = regPhone.firstName.data
        lastName = regPhone.lastName.data
        phoneNum = regPhone.phoneNum.data
        email = regPhone.email.data
        address = regPhone.address.data
        city = regPhone.city.data
        state = regPhone.state.data
        print(firstName, phoneNum)
    return render_template('registerPhone.html',title=title, regPhone=regPhone)
