import os
here = os.path.dirname(os.path.abspath(__file__))

from flask import Flask
app = Flask("lazy-snake", template_folder=here+"/views")
app.secret_key = "jklpuzo"
