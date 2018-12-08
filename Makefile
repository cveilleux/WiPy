init:
		pipenv install --dev

test:

		pipenv run pytest tests
		pipenv run black --check --diff pyric/