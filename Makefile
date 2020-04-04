start_dev:
	FLASK_APP=app/start_app.py \
	FLASK_ENV=development \
	SECRET_KEY=$(SECRET_KEY) \
	python3 -m flask run --host=0.0.0.0

run_tests:
	python -m pytest

build_image:
	docker build -t climbing_stats_img .

docker_dev:
	docker run \
	--name climbing_stats_container \
	--rm \
	-p 5000:5000 \
	climbing_stats_img