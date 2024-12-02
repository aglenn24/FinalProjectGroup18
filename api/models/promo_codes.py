from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PromoCodes(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo = Column(String(25), unique=True, nullable=False)
    discount_percent = Column(DECIMAL(3, 2), CheckConstraint("discount_percent >= 0 AND discount_percent <= 100"), nullable=False)
    expiration = Column(DATETIME, unique=False, nullable=False)

    orders = relationship("Order", back_populates="promo_code")