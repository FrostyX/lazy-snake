from app import app
from flask import render_template
from app.models.CPythonParser import CPythonParser
from app.tests.test_CPythonParser import input

@app.route('/')
@app.route('/home')
def get_home():
	stats = CPythonParser().parse(input)
	return render_template('home.html', stats=stats)

@app.route('/about')
def get_about():
	return render_template('about.html')

@app.route('/feedback')
def get_feedback():
	return render_template('feedback.html')
