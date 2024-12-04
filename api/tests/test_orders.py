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

    order_data_full = {
        "customer_name": "John Doe",
        "customer_address": "123 Main St",
        "customer_email": "<EMAIL>",
        "customer_phone": "123-456-7890",
        "description": "Test order",
        "tracking_number": "12345",
        "order_status": "Good",
        "order_date": "2023-01-01",
        "total_price": "100.00",
        "review_text": "Test Review",
        "score": "4.0",
        "card_info": "0000000000000000",
        "transaction_status": "Pending",
        "payment_type": "Credit Card"
    }

    order_object = model.Order(**order_data)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.description == "Test order"
    assert created_order.tracking_number == "12345"
    assert created_order.order_status == "Good"
    assert created_order.order_date == "2023-01-01"
    assert created_order.total_price == "100.00"
    assert created_order.review_text == "Test Review"
    assert created_order.score == "4.0"
    assert created_order.card_info == "0000000000000000"
    assert created_order.transaction_status == "Pending"
    assert created_order.payment_type == "Credit Card"
