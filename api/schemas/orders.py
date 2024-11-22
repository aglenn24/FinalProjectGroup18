from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    # customer info
    customer_name: str
    customer_address: str
    customer_email: str
    customer_phone: str
    description: Optional[str] = None
    
    # order info
    tracking_number: int
    order_status: str
    order_date: datetime
    total_price: float
    
    # review
    review_text: Optional[str] = None
    score: float
    
    # payment info
    card_info: str
    transaction_status: str
    payment_type: str
    

class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
