from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, CheckConstraint, Sequence
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base



class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    
    # order contents
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, index=True, nullable=False)
    
    order = relationship("Order", back_populates="order_detail")
    sandwich = relationship("Sandwich", back_populates="order_detail")
