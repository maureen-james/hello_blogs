from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo
from ..models import User
# from wtforms import ValidationError



class FormCategory(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
   
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[DataRequired(), Length(1, 64)])
    category = StringField('Blog Category', validators=[DataRequired(), Length(1, 64)])
    post = TextAreaField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Blog Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
