from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import *
from .forms import BlogForm, CommentForm, UpdateProfile
from ..models import Blog,Comment,Likes,Dislikes
from .. import db
from ..request import get_quote
from flask_login import login_required,current_user

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

@main.route('/new_blog', methods = ['POST','GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_blog_object = Blog(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_blog_object.save()
        return redirect(url_for('main.index'))
        
    return render_template('new_blog.html', form = form)

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        new_comment = Comment(comment=comment,blog_id = blog_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html',form = form, blog = blog,all_comments=all_comments)  


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)    

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_blog = Likes.get_likes(id)
    valid_string = f'{current_user.id}:{id}'
    for blog in get_blog:
        to_str = f'{blog}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Likes(user = current_user, blog_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    blog = Dislikes.get_dislikes(id)
    valid_string = f'{current_user.id}:{id}'
    for b in blog:
        to_str = f'{b}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_dislike = Dislikes(user = current_user, blog_id=id)
    new_dislike.save()
    return redirect(url_for('main.index',id = id))  

@main.route('/delete_blog/<int:id>',methods = ['GET','POST'])
@login_required
def delete(id):
    blog= Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route("/delete_comment/<int:id>")
@login_required
def delete_comment(id):
    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('main.index'))      
