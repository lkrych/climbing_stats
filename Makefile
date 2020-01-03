start_dev:
	FLASK_APP=app/climbing_stats.py \
	FLASK_ENV=development \
	SECRET_KEY=$(SECRET_KEY) \
	python -m flask run
