from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class NewdeviceForm(FlaskForm):
    members_in_stack = StringField('Number of stack members')
    uplinks = StringField('Number of uplinks')
    vlan_interco_vdl = StringField('VDL interco VLANID')
    second_byte_mgmt_vdl = StringField('Second byte Mgmt IP')
    third_byte_mgmt_vdl = StringField('Third byte Mgmt IP')
    fourth_byte_mgmt_vdl = StringField('Fourth byte Mgmt IP')
    second_byte_interco_tl = StringField('Second byte IP Interco TL')
    third_byte_interco_tl = StringField('Third byte IP Interco TL')
    third_byte_hc = StringField('Third byte IP Hotcity')
    hostname = StringField('Hostname')
    accessport_nb = StringField('Number of switch ports')
    snmp_location = StringField('SNMP Location')
    submit = SubmitField('Create')
