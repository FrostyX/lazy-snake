import os
from app import app
from flask import render_template, request, redirect, url_for
from app.config import UPLOAD_DIR
from app.models import Hash
from app.models.CPythonParser import CPythonParser
from app.models.Stats import parameters
from app.tests.test_CPythonParser import input

RESULTS_DIR = UPLOAD_DIR + "results"


@app.route('/', methods=["GET"])
def get_home():
	return render_template("home.html")


@app.route('/', methods=["POST"])
def post_home():
	file = request.files["result"]
	name = Hash.make()
	file.save(os.path.join(RESULTS_DIR, name))
	return redirect("/result/" + name)


@app.route('/result/<name>/')
@app.route('/result/<name>/<sort>/')
@app.route('/result/<name>/<sort>/<direction>/')
def get_result(name, sort="cumtime", direction="asc"):
	stats = CPythonParser().parse(input)

	return render_template('profile.html',
	   controller = "result/" + name,
	   stats=stats,
	   parameters=parameters,
	   sort=sort,
	   direction=(direction == "desc")
	)


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
