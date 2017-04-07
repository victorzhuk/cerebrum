SHELL=/bin/sh

init:
	#@pip install --user -r requirements.txt

test:
	@python -m unittest discover -s test -p "*_test.py"

.PHONY: init test
