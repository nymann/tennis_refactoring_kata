install:
	@pip install -e '.[dev]'

test: install
	@python setup.py test
