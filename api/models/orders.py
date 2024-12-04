from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Sequence
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base



class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # order contents
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, index=True, nullable=False)
    
    # payment info
    card_info = Column(String(25), nullable=True)  
    transaction_status = Column(
        String(20),
        nullable=False,
        default="Pending"
    )
    payment_type = Column(String(50), nullable=True)  
    
    order_details = relationship("OrderDetail", back_populates="order")
    sandwiches = relationship("Sandwich", back_populates="order")
