init:
		pipenv install --dev

test:

		pipenv run pytest tests
		pipenv run yapf -rdp pyric/