from flask import render_template
from flask_boilerplate import app

@app.errorhandler(404)
def error_han(e):
	return "404 not found"

@app.route('/')
def home():
	return render_template('home.html')
