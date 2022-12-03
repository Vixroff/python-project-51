install:
	poetry install

build:
	poetry build

packadge-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

run:
	poetry run page-loader https://meplant.ru