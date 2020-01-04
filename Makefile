start_dev:
	FLASK_APP=app/start_app.py \
	FLASK_ENV=development \
	SECRET_KEY=$(SECRET_KEY) \
	python -m flask run

run_tests:
	python -m pytest
