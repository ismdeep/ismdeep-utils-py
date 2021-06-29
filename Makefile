install:
	pip3.9 install twine
	pip3.9 install -r requirements.txt

build:
	python3.9 setup.py sdist

upload:
	twine upload dist/*
