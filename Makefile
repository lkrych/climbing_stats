start_dev:
	FLASK_APP=app/climbing_stats.py \
	FLASK_ENV=development \
	python -m flask run

create_db:
	cd db 
	python init_db.py