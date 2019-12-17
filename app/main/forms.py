from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_babel import _, lazy_gettext as _l
from app.models import User

class EditProfileForm(FlaskForm):
    section = [('Beavers', 'Beavers'), ('Cubs', 'Cubs'), ('Scouts', 'Scouts'), ('No Section (N/A)', 'N/A')]
    leader_choice = [('Yes', 'Yes'), ('No', 'No')]
    username = StringField(_l('Username', validators=[DataRequired()]))
    email = StringField(_l('Email', validators=[DataRequired(), Length(min=5, max=40)]))
    childs_section = SelectField(u'Childs Section', choices=section, validators=[DataRequired()])
    leader = SelectField(u'Are you a Leader?', choices=leader_choice, validators=[DataRequired()])
    about_me = TextAreaField(_l('About me', validators=[Length(min=0, max=140)]))
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username'))

class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something', validators=[DataRequired(), Length(min=1, max=140)]))
    #post_attachments = FileField(_l('Upload Attachments', validators=[FileRequired('No file Selected!')]))
    submit = SubmitField(_l('Submit'))

class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))