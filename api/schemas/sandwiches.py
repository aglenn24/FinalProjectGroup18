from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float


class SandwichCreate(SandwichBase):
    sandwich_name: str
    price: float
    calories: int
    food_category: str
    description: str


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None
    calories: int
    food_category: str
    description: str
    

class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True