from flask import session, render_template, request, redirect, flash
import json
from flask_app import app

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/CV')
def cv():
    return render_template("cv.html")

@app.route('/About')
def about():
    return render_template('about.html')