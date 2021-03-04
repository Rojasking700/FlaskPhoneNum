from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class RegisterPhoneForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    phoneNum = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPass = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()
    
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()

