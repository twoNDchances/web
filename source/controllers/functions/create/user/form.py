from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=5, max=16)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=16)])
    cf_pword = PasswordField(label='Confirm Password', validators=[EqualTo(fieldname='password')])
    submit_button = SubmitField(label='Register')
