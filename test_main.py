from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)


def test_prediccion():
    response = client.post("/predict",
                           json={
                               "OPERA": "Aerolineas Argentinas",
                               "MES": 1,
                               "TIPOVUELO": "I"
                           })
    assert response.status_code == 200
