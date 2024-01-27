from fastapi.testclient import TestClient
import sys
sys.path.insert(0, './src')
from app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Test Pipeline Project"}

def test_predict_sentiment_valid_input():
    # Test prediction endpoint with valid input
    data = {"phrase": "Hello, this is a valid phrase."}
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_sentiment_invalid_input():
    # Test prediction endpoint with invalid input
    data = {"phrase": 12}
    response = client.post("/predict", json=data)
    assert response.status_code == 422