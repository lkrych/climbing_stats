start_dev:
	FLASK_APP=app/climbing_stats.py \
	python -m flask run

create_db:
	cd db 
	python init_db.py