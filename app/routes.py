from app import app, db, mail, Message
from flask import render_template, request, flash, redirect, url_for
from app.forms import RegisterPhoneForm, LoginForm
from app.model import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    context = {
        'title' : 'HOME',
        'users' : User.query.order_by(User.firstName).all()
    }
    return render_template('index.html', **context)

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

@app.route('/myinfo')
@login_required
def myinfo():
    title = "My Info"
    # user = current_user.User
    return render_template('myinfo.html', title=title)

@app.route('/myinfo/<int:user_id>')
@login_required
def myinfodetail(user_id):
    user = User.query.get_or_404(user_id)
    title = f"My Info {user.id}"
    return render_template('myinfodetail.html', user=user, title=title)

@app.route('/myinfo/update/<int:user_id>', methods=['GET','POST'])
@login_required
def myinfoupdate(user_id):
    title = "My Info Update"
    user = User.query.get_or_404(user_id)
    update_form = RegisterPhoneForm()

    if user.id != current_user.id:
        flash("You can not update another user's info", 'danger')
        return redirect(url_for('myinfo'))

    if request.method == "POST" and update_form.validate():
        username = regPhone.username.data
        firstName = regPhone.firstName.data
        lastName = regPhone.lastName.data
        phoneNum = regPhone.phoneNum.data
        email = regPhone.email.data
        address = regPhone.address.data
        city = regPhone.city.data
        state = regPhone.state.data
        password = regPhone.password.data

        user.username = username
        user.firstName = firstName
        user.lastName = lastName
        user.phoneNum = phoneNum
        user.email = email
        user.address = address
        user.city = city
        user.state = state
        user.password = password

        db.session.commit()
        flash("Your information has been updated!")
        return redirect(url_for('myinfodetail'))
    return render_template('myinfoupdate.html', form=update_form, title=title)

@app.route('/myinfo/delete/<int:user_id>', methods=['GET','POST'])
@login_required
def myinfodelete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    if user.id != current_user.id:
        flash("You cannot delete another users info", 'danger')
        return redirect(url_for('index'))

    flash('This sccount has been deletes', 'info')
    return redirect(url_for('index'))