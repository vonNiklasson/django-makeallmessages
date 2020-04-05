# Environment setup

.PHONY: env-create
env-create:
	virtualenv -p python3 .venv
	make env-update

.PHONY: env-update
env-update:
	bash -c ". .venv/bin/activate; pip install --upgrade -r requirements.txt;"

.PHONE: env-delete
env-delete:
	rm -rf .venv


# Linting and reformatting

.PHONY: lint
lint:
	python -m pycodestyle . --exclude '.venv,setup.py,docs/*'
	isort --recursive --check-only makeallmessages tests
	black --check makeallmessages tests
	pylint makeallmessages
	pylint --disable=missing-docstring,no-self-use tests/*
	mypy makeallmessages

.PHONY: reformat
reformat:
	isort --recursive makeallmessages tests
	black makeallmessages tests

