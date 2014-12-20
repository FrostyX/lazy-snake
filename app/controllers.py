from app import app
from flask import render_template
from app.models.CPythonParser import CPythonParser
from app.models.Stats import parameters
from app.tests.test_CPythonParser import input

@app.route('/')
def get_home():
	return render_template("home.html")

@app.route('/demo')
@app.route('/demo/<sort>/')
@app.route('/demo/<sort>/<direction>/')
def get_demo(sort="cumtime", direction="asc"):
	stats = CPythonParser().parse(input)

	return render_template('profile.html',
	    controller = "demo",
	    stats=stats,
	    parameters=parameters,
	    sort=sort,
	    direction=(direction == "desc")
	)

@app.route('/about/')
def get_about():
	return render_template('about.html')

@app.route('/feedback/')
def get_feedback():
	return render_template('feedback.html')
