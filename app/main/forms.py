# from flask_wtf import FlaskForm
# from wtforms import StringField,TextAreaField,SubmitField
# from wtforms.validators import DataRequired,Email,EqualTo
# from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField
# from ..models import User
# from wtforms import ValidationError

# class ReviewForm(FlaskForm):

#     title = StringField('Review title',validators=[DataRequired()])
#     review = TextAreaField('Movie review', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# class RegistrationForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[DataRequired(),Email()])
#     username = StringField('Enter your username',validators = [DataRequired()])
#     password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
#     password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
#     submit = SubmitField('Sign Up') 

#     def validate_email(self,data_field):
#             if User.query.filter_by(email =data_field.data).first():
#                 raise ValidationError('There is an account with that email')

#     def validate_username(self,data_field):
#         if User.query.filter_by(username = data_field.data).first():
#             raise ValidationError('That username is taken')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField, FileField,TextAreaField
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


class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[DataRequired(), Length(1, 64)])
    category = StringField('Pitch Category', validators=[DataRequired(), Length(1, 64)])
    post = TextAreaField('Pitch Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    content = TextAreaField('Pitch Content', validators=[DataRequired()])
    submit = SubmitField('Submit')
