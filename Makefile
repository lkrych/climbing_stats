DATABASE_URL := sqlite:///db/climbing_stats.db

start:
	FLASK_APP=app/climbing_stats.py \
	DATABASE_URL=$(DATABASE_URL) \
	python -m flask run

create_db:
	cd db 
	python init_db.py