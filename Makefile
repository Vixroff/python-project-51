build:
	poetry build

packadge-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest

run:
	poetry run page-loader https://www.google.com