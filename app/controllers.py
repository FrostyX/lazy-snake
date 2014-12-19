from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def get_home():
	return render_template('home.html', title='Home')

@app.route('/about')
def get_about():
	return render_template('about.html')

@app.route('/feedback')
def get_feedback():
	return render_template('feedback.html')
