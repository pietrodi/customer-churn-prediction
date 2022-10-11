IMG_NAME := churn-prediction
IMG_TAG := dev
DOCKER_BUILD_CONTEXT="."

.PHONY: build
build:
	docker build -t $(IMG_NAME):$(IMG_TAG) .

.PHONY: run-with-docker
run-with-docker: 
	make build
	docker run -p 9696:9696 -it $(IMG_NAME):$(IMG_TAG)
	
.PHONY: train
train:
	pipenv run python scripts/train.py

.PHONY: dev
dev:
	pipenv run waitress-serve --listen=0.0.0.0:9696 predict:app

.PHONY: request
request:
	pipenv run python scripts/request.py