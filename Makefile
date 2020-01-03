start_dev:
	FLASK_APP=app \
	FLASK_ENV=development \
	SECRET_KEY=$(SECRET_KEY) \
	python -m flask run
