from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromoCodeBase(BaseModel):
    promo: str
    expiration: datetime
    discount_percent: float

class PromoCodeCreate(PromoCodeBase):
    pass

class PromoCodeUpdate(BaseModel):
    promo: Optional[str] = None
    expiration: Optional[datetime] = None
    discountPercent: Optional[float] = None

class PromoCode(PromoCodeBase):
    id: int

    class ConfigDict:
        from_attributes = True
