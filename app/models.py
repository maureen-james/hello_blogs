from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# user table
class User(UserMixin, db.Model):  
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    blog=db.relationship('Blog',backref='user',lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    likes = db.relationship('Likes', backref='user', lazy='dynamic')
    dislikes = db.relationship('Dislikes', backref='user', lazy='dynamic')


    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    post = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment', backref='blog', lazy='dynamic')
    category = db.Column(db.String(255), index = True,nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.relationship('Likes', backref='blog', lazy='dynamic')
    dislikes = db.relationship('Dislikes', backref='blog', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Blog {self.title}"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    comment = db.Column(db.Text(),nullable = False) 
    
    def save_c(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()
        return comments

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment: {self.comment}'

class Quote:
    """
    Class that returns quotes requested from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
            

class Likes(db.Model):
  _tablename_ = 'likes'
  id = db.Column(db.Integer,primary_key=True)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
  def save(self):
    db.session.add(self)
    db.session.commit()
  @classmethod
  def get_likes(cls,id):
    like = Likes.query.filter_by(blog_id=id).all()
    return like
  def _repr_(self):
      return f'{self.user_id}:{self.blog_id}'


class Dislikes(db.Model):
  _tablename_ = 'dislikes'
  id = db.Column(db.Integer,primary_key=True)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
  def save(self):
    db.session.add(self)
    db.session.commit()
  @classmethod
  def get_dislikes(cls,id):
    dislikes = Dislikes.query.filter_by(blog_id=id).all()
    return dislikes
  def _repr_(self):
      return f'{self.user_id}:{self.blog_id}'        