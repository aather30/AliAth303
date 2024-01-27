# ML Challenge


## Description

The following project consists of a trained model which is being used to classify a phrase into one of the six labels.

The web framework used for building the API is FastAPI. The `predict` method uses the trained model and predict the class of the input through the model. The application is dockerized as well.

The test coverage of the API code can be seen in the HTML page located in the following path `htmlcov/index.html`. The coverage is also shown in the `problem_solving_approach` file.

The approach of the project is discussed in detail in the file named `problem_solving_approach.docx`.


## How to Setup

You need to build and run the Docker container to run the API. You should be at the root level of the directory where the `Dockerfile` is located.
- Build the Image using the following command:
```sh
docker build -t fastapi-docker-ml .
```
- Run the Docker container:
```sh
docker run -d -p 8000:8000 fastapi-docker-ml
```

You can also run the API directly following these steps:

1. Create the environment
```sh
python3 -m venv ./venv
```
2. Activate the environment
```sh
source ./venv/bin/activate
```
3. Install dependencies (make sure you are using the latest version of pip)
```sh
pip3 install -r requirements.txt
```
4. Run py file
```sh
python src/app.py
```


## How to use
- Post Endpoint for prediction
```ssh
127.0.0.0.1/predict
```

- Request Example
```json
{
   "phrase": "geländer biegen"
}
```
- Response Example
```json
{
   "prediction": ["mr"]
}
```

- An example of a `CURL` call could be as follows:
```sh
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"phrase": "technische"}'
```