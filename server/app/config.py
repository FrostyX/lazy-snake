import os

parent = os.path.dirname(os.path.dirname(__file__))
UPLOAD_DIR = os.environ.get("OPENSHIFT_DATA_DIR", parent + "/storage/")
RESULTS_DIR = UPLOAD_DIR + "results"
