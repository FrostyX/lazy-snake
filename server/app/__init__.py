import os
from flask import Flask


here = os.path.dirname(os.path.abspath(__file__))
app = Flask("lazy-snake",
	template_folder=here+"/views",
	static_folder=here+"/../static"
)
app.secret_key = os.environ.get("OPENSHIFT_SECRET_TOKEN", "jklpuzo")
