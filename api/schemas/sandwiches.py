from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None
    calories: int
    food_category: str
    description: str

class SandwichCreate(SandwichBase):
    pass


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