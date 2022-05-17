# from . import main
# from flask import render_template,request,redirect,url_for,abort
# from ..models import Blog




# # @main.route('/')
# # def index():
# #     return render_template('index.html')
# @main.route('/')
# def index():
#     blog=Blog.query.all()

#     return render_template('index.html', blog=blog)
    
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import *
from ..models import Blog,Comment
from .. import db
from ..request import get_quote

# from flask_login import login_required,current_user

@main.route('/')
def index():
    blog=Blog.query.all()
    quote = get_quote()

    return render_template('index.html', blog=blog, quote=quote)

@main.route('/addblog',methods=['GET','POST'])
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(title=form.title.data, content=form.content.data, author=form.author.data) 
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('blogs.html', form=form)

@main.route('/addcomment',methods=['GET','POST'])
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(title=form.title.data, content=form.content.data, username=form.username.data) 
        db.session.add(new_comment)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('comment.html', form=form)    