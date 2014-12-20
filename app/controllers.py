from app import app
from flask import render_template
from app.models.CPythonParser import CPythonParser
from app.models.Stats import parameters
from app.tests.test_CPythonParser import input

@app.route('/')
@app.route('/<sort>/')
@app.route('/<sort>/<direction>/')
def get_home(sort="cumtime", direction="asc"):
	stats = CPythonParser().parse(input)

	return render_template('home.html',
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
