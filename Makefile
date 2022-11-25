build:
	poetry build

packadge-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 page_loader