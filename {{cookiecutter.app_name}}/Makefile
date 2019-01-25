default: test

endpoint:
	curl http://localhost:5000/api/v1/

init:
	pipenv install

init-dev:
	pipenv install -d

lock-requirements:
	pipenv lock -r > requirements.txt

run-app:
	FLASK_APP={{ cookiecutter.app_name }}.app FLASK_ENV=development \
	pipenv run flask run

run-test:
	pipenv run pytest --flake8 --black --cov={{ cookiecutter.app_name }} --cov-report term-missing tests/

r: run-app
run: init r
t: run-test
test: init-dev t
