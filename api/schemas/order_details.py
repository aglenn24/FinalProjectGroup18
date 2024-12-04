from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    sandwich_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    sandwich_id: int 
    customer_name: Optional[str] = None
    customer_address: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    description: Optional[str] = None
    tracking_number: Optional[int] = None
    order_status: Optional[str] = None
    order_date: Optional[datetime] = None
    review_text: Optional[str] = None
    score: Optional[float] = None

    
    sandwich: Optional[Sandwich] = None 
    
class ConfigDict:
        from_attributes = True
