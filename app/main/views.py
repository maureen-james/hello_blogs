from app import main
from flask import render_template,request,redirect,url_for,abort




@main.route('/')
def index():
    return render_template('index.html')