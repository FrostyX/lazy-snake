import os


UPLOAD_DIR = os.environ.get("OPENSHIFT_DATA_DIR", "storage/")
RESULTS_DIR = UPLOAD_DIR + "results"
