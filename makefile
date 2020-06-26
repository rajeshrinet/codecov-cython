PYTHON=python 

cycov:
	python setup.py build_ext --force --inplace --define CYTHON_TRACE
	pytest test.py  --cov=./ --cov-report=xml

test:
	@echo testing...
	python test.py
