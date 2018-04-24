from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, BooleanField
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
    device_model = SelectField('Select device model', choices = [('0', 'Select model'),('1', 'Catalyst 3650'),('2', 'Catalyst 3560CX'),('3', 'Catalyst 3560CG'),('4', 'ISRG3 4321')])
    tunnel_address = StringField('Tunnel Address')
    site_code = StringField('Site Code')
    members_in_stack = StringField('Number of stack members')
    uplinks = StringField('Number of uplinks')
    is_l3 = BooleanField('L3 device')
    vlan_interco_vdl = StringField('VDL interco VLANID')
    second_byte_mgmt_vdl = StringField('Second byte Mgmt IP')
    third_byte_mgmt_vdl = StringField('Third byte Mgmt IP')
    fourth_byte_mgmt_vdl = StringField('Fourth byte Mgmt IP')
    has_tl = BooleanField('Technolink')
    second_byte_interco_tl = StringField('Second byte IP Interco TL')
    third_byte_interco_tl = StringField('Third byte IP Interco TL')
    has_hc = BooleanField('Hotcity')
    third_byte_hc = StringField('Third byte IP Hotcity')
    hostname = StringField('Hostname')
    accessport_nb = StringField('Number of switch ports')
    snmp_location = StringField('SNMP Location')
    easyqos_profile = SelectField('Select QoS profile', choices = [('1', 'Default profile'),('2', 'VOIP profile')])
    submit = SubmitField('Create')
