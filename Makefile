help:
	@echo "Please use \`make <target>' where <target> is one of these"
	@echo "  test           to run all automated tests for this project"

test:
	nosetests -d
