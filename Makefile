FLASK_APP := climbing_stats_backend

backend-dev:
	FLASK_APP=${FLASK_APP} \
	FLASK_ENV=development \
	ENV=development \
	python3 -m flask run --host=0.0.0.0

frontend-dev:
	cd frontend && npm start

test:
	pytest --setup-show

build-image-dev:
	docker build -t climbing_stats_img . -f Dockerfile.dev

docker-dev: build-image-dev
	docker run \
	--name climbing_stats_container \
	--rm \
	-p 5000:5000 \
	-it \
	climbing_stats_img

init-db:
	cd db && python init_db.py
	FLASK_APP=${FLASK_APP} \
	ENV=development \
	flask reset-db
	FLASK_APP=${FLASK_APP} \
	ENV=development \
	flask seed-db

build-image-prod:
	docker build -t climbing_stats_img . -f Dockerfile.prod

backend-prod:
	FLASK_APP=${FLASK_APP} \
	ENV=production \
	gunicorn -b 0.0.0.0:80 "climbing_stats_backend:create_app()" --access-logfile=-

docker-prod: build-image-prod
	docker run \
	--name climbing_stats_container \
	--rm \
	-p 5000:80 \
	-it \
	climbing_stats_img