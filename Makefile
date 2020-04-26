FLASK_APP := climbing_stats_backend

start-dev:
	FLASK_APP=${FLASK_APP} \
	FLASK_ENV=development \
	SECRET_KEY=$(SECRET_KEY) \
	python3 -m flask run --host=0.0.0.0

start-local:
	FLASK_APP=${FLASK_APP} \
	FLASK_ENV=development \
	SECRET_KEY=$(SECRET_KEY) \
	python3 -m flask run 

start-frontend:
	cd frontend && npm start

run-tests:
	python -m pytest

build-image:
	docker build -t climbing_stats_img .

docker-dev: build_image
	docker run \
	--name climbing_stats_container \
	--rm \
	-p 5000:5000 \
	climbing_stats_img

init-db:
	cd db && python init_db.py
	flask seed-db