all: build
clean:
	rm -rf build
cleanvenv:
	rm -rf venv

venv: venv/bin/python

venv/bin/python: requirements.txt
	test -f $@ || virtualenv2 --no-site-packages venv
	./venv/bin/pip install -Ur requirements.txt

build: venv manage.py app.py discovery.py $(shell find templates/ static/ -type f)
	rm -rf build
	./venv/bin/python manage.py freeze
