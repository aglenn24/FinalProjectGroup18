import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_valid_order():
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "item": "Sandwich", "quantity": 2}

def test_get_invalid_order():
    response = client.get("/orders/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Order not found"}
