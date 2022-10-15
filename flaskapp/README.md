# Prediction app

The code in this folder can be used to run a Flask based webserver which serves the machine learning customer churn prediction model.

## Requirements

In order to run the app you will need to have [pipenv](https://pypi.org/project/pipenv/) installed. Additionally, if you want to run the app with docker you will need to have [Docker](https://www.docker.com/) installed. Also, you will need to train and save the prediction model  to the flaskapp folder before running the app, which can be done as follows.

### Install dependencies

First you will need to run this command to install required dependecies:

```sh
pipenv install
```

### Training the model

Then you will need to run this command to train and save the model:

```sh
make train
```

At this point you should have a ```model.pkl``` file in the flaskapp folder.

## Running locally

The below command will run the application locally: 

```sh
make dev
```

## Running with Docker

The below command will both build the Docker image and run it:

```sh
make run-with-docker
```

## Example call to the service

### Using Python

```python
import requests

LOCAL_URL = 'http://localhost:9696/predict'
SAMPLE_CUSTOMER = {
    'CustomerId': 83131903810,
    ...
}

requests.post(LOCAL_URL, json = SAMPLE_CUSTOMER).json()
```

This is sample code for a request to the service, full code can be found [here](./scripts/request.py) and can be run with command: `make request`.