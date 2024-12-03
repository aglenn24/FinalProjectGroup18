from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_name": "John Doe",
        "description": "Test order"
    }

    order_object = model.Order(**order_data)

    created_order = controller.create(db_session, order_object)

    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.description == "Test order"


def test_get_valid_order(db_session, mocker):
    mock_order = {
        "id": 1,
        "customer_name": "John Doe",
        "description": "Test order"
    }

    mocker.patch("..controllers.orders.read_one", return_value=mock_order)

    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "customer_name": "John Doe",
        "description": "Test order"
    }


def test_get_invalid_order(db_session, mocker):
    mocker.patch("..controllers.orders.read_one", return_value=None)

    response = client.get("/orders/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Order not found"}
