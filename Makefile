
all:
	@echo "make install - Install on local system"
	@echo "make test - Run tests during development"
	@echo "make performance - Run performance test of this and other implementation"
	@echo "make doc - Make documentation"
	@echo "make clean - Get rid of scratch and byte files"


deb:
	python setup.py --command-packages=stdeb.command bdist_deb

upload:
	python setup.py register sdist upload

install:
	pip install --editable .[test]

test:
	python -m pytest tests

performance:
	python performance.py

doc:
	cd docs; make

clean:
	python setup.py clean
	find . -name '*.pyc' -delete
