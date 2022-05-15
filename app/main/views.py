from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import Blog




# @main.route('/')
# def index():
#     return render_template('index.html')
@main.route('/')
def index():
    blog=Blog.query.all()

    return render_template('index.html', blog=blog)    