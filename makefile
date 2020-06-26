
PYTHON = ~/software/anaconda/bin/python

all: matMul.so

matMul.so: matMul.pyx
	$(PYTHON) setup.py build_ext --inplace

clean:
	rm -rf build matMul.so matMul.c matMul.html 

cycov:
	python setup.py build_ext --force --inplace --define CYTHON_TRACE
	pytest test.py  --cov=./ --cov-report=xml


test:
	@echo testing...
	python test.py
