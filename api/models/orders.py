from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Sequence
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    # Primary key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Customer info
    customer_name = Column(String(100), nullable=False)
    customer_address = Column(String(100), nullable=False)
    customer_email = Column(String(50), nullable=False)
    customer_phone = Column(String(20), nullable=False)
    description = Column(String(300), nullable=True)

    # Order details
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, nullable=False)
    tracking_number = Column(String(100), nullable=False, unique=True)
    order_status = Column(String(20), nullable=False, default="Pending")
    order_date = Column(DATETIME, nullable=False, default=datetime.now)
    total_price = Column(DECIMAL(10, 2), nullable=False)

    # Review info
    review_text = Column(String(500), nullable=True, default="")
    score = Column(DECIMAL(2, 1), nullable=True, default=3)

    # Payment info
    card_info = Column(String(25), nullable=True)
    transaction_status = Column(String(20), nullable=False, default="Pending")
    payment_type = Column(String(50), nullable=True)

    # Relationships
    order_details = relationship("OrderDetail", back_populates="order")
    sandwiches = relationship("Sandwich", back_populates="order")
