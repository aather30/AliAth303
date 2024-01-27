import uvicorn
from fastapi import FastAPI
import joblib
import sys
sys.path.insert(0, './src')
from schemas.schemas import Phrase
import json


# Reading configuration file
config_path = "configs/config.json"

with open(config_path, 'r') as json_file:
    config = json.load(json_file)

app = FastAPI()

# Loading the TF-IDF model
loaded_tfidf_model = joblib.load(f'./{config["model_path"]}tfidf_model.joblib')
# Loading the SVM model
loaded_svm_model = joblib.load(f'./{config["model_path"]}svm_model.joblib')


@app.get('/')
def index():
    return {'message': 'Test Pipeline Project'}

@app.post('/predict')
def predict_sentiment(req:Phrase):

    req = req.dict()
    phrase = req["phrase"]
    vectorized_input = loaded_tfidf_model.transform([phrase])

    result = loaded_svm_model.predict(vectorized_input)

    return {
        'prediction': result.tolist()
    }
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)