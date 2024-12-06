from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    calories = Column(Integer)
    food_category = Column(String(255))
    description = Column(String(255), nullable=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    recipe = relationship("Recipe", back_populates="sandwiches")
    order_details = relationship("OrderDetails", back_populates="sandwiches")
    orders = relationship("Order", back_populates="sandwiches")