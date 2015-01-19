import os
import urllib2
from . import app
from flask import render_template, request, redirect, url_for, flash
from config import RESULTS_DIR
from models import Hash
from models.CPythonParser import CPythonParser
from models.Stats import parameters
from tests.test_CPythonParser import input


@app.route('/', methods=["GET"])
def get_home():
	return render_template("home.html")


@app.route('/', methods=["POST"])
def post_home():
	def error():
		flash("Please post your profiler result via file or url")
		return redirect("/")

	name = Hash.make()
	r_ok = redirect("/result/" + name)

	if "post_file" in request.values:
		file = request.files["result"]
		if not file:
			return error()

		file.save(os.path.join(RESULTS_DIR, name))
		return r_ok

	elif "post_url" in request.values:
		url = request.values["url"]
		if not url:
			return error()

		response = urllib2.urlopen(url)
		content = response.read()
		with open(RESULTS_DIR + "/" + name, "w") as f:
			f.write(content)
		return r_ok


@app.route('/result/<name>/')
@app.route('/result/<name>/<sort>/')
@app.route('/result/<name>/<sort>/<direction>/')
def get_result(name, sort="cumtime", direction="asc"):
	f = open(RESULTS_DIR + "/" + name, "r")
	stats = CPythonParser().parse(f.read())

	return render_template('profile.html',
	   name=name,
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


@app.route('/delete/<name>/')
def get_delete(name):
	os.remove(RESULTS_DIR + "/" + name);
	return redirect("/")


@app.route('/about/')
def get_about():
	return render_template('about.html')


@app.route('/feedback/')
def get_feedback():
	return render_template('feedback.html')
