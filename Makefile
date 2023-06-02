APP_NAME="gs-neuromorphic"
IMAGE_NAME="eduardomatoss/gs-neuromorphic"
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    DOCKER_USER=$(shell id -u $(USER)):$(shell id -g $(USER))
endif
ifeq ($(UNAME_S),Darwin)
    DOCKER_USER=
endif

################################
# COMMANDS TO RUN LOCALLY
################################

local/install: generate-default-env-file
	poetry install

local/bandit:
	bandit -r . app *.py

local/lint:
	poetry run flake8 app/
	poetry run black --check app/

local/lint/fix:
	poetry run black app/

local/run:
	poetry run streamlit run run.py


############################################
# COMMANDS TO RUN USING DOCKER (RECOMMENDED)
############################################

docker/build: generate-default-env-file
	docker-compose build ${APP_NAME}

docker/up:
	docker-compose up -d

docker/postgres/up:
	CURRENT_UID=${DOCKER_USER} docker-compose up -d postgres-db

docker/down:
	docker-compose down --remove-orphans

docker/bandit:
	CURRENT_UID=${DOCKER_USER} docker-compose run ${APP_NAME} poetry run bandit -r . app *.py

docker/lint:
	docker-compose run ${APP_NAME} poetry run flake8 app/
	docker-compose run ${APP_NAME} poetry run black --check app/

docker/lint/fix:
	docker-compose run ${APP_NAME} poetry run black app/

docker/run: docker/postgres/up docker/migrations/upgrade
	docker-compose run ${APP_NAME} poetry run streamlit run run.py

docker/migrations/generate:
	CURRENT_UID=${DOCKER_USER} docker-compose run ${APP_NAME} poetry run alembic revision --autogenerate

docker/migrations/upgrade:
	CURRENT_UID=${DOCKER_USER} docker-compose run ${APP_NAME} poetry run alembic upgrade head

##################
# HELPFUL COMMANDS
##################

image/build:
	docker build . --target production -t ${IMAGE_NAME}:${VERSION}

image/push:
	docker push ${IMAGE_NAME}:${VERSION}

generate-default-env-file:
	@if [ ! -f .env ]; then cp env.template .env; fi;
