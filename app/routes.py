from app import app, db, mail, Message
from flask import render_template, request, flash, redirect, url_for
from app.forms import RegisterPhoneForm, LoginForm
from app.model import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    title = 'index'
    return render_template('index.html', title=title)

@app.route('/RegisterPhoneNum', methods=['GET','POST'])
def RegisterPhoneNum():
    title = 'Register Phone Number'
    regPhone = RegisterPhoneForm()
    if request.method == 'POST' and regPhone.validate:
        username = regPhone.username.data
        firstName = regPhone.firstName.data
        lastName = regPhone.lastName.data
        phoneNum = regPhone.phoneNum.data
        email = regPhone.email.data
        address = regPhone.address.data
        city = regPhone.city.data
        state = regPhone.state.data
        password = regPhone.password.data

        print(username, firstName)

        new_user = User(username, firstName, lastName, phoneNum, email, address, city, state, password)
        db.session.add(new_user)
        db.session.commit()

        msg = Message(f"Welcome, {username}", [email])
        msg.html = "<p>You have now signed up for a useless phonebook! Enjoy the junk mail we will be sending you!!!!</p>"
        mail.send(msg)

        flash("You have successfully signed up!","success")
        return redirect(url_for('index'))


    return render_template('registerPhone.html',title=title, regPhone=regPhone)


@app.route('/login', methods=['GET','POST'])
def login():
    title = "Login"
    form = LoginForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            flash("Incorrect Email/Password. Please try again foo!")
            return redirect(url_for('login'))
        
        login_user(user,remember=form.remember_me.data)
        flash("You have successfully logged in!", 'success')
        next_page = request.args.get('next')
        if next_page:
            return redirect(url_for(next_page.lstrip('/')))
        return redirect(url_for('index'))

    return render_template('login.html',title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("you have successfully logged out", 'primary')
    next_page = request.args.get('next')
    if next_page:
        return redirect(url_for(next_page.lstrip('/')))
    return redirect(url_for('index'))