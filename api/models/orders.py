from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # customer info
    customer_name = Column(String(100))
    customer_address = Column(String(100))
    customer_email = Column(String(50))
    customer_phone = Column(String(20))
    description = Column(String(300))
    
    # order info
    tracking_number = Column(Integer)
    order_status = Column(String(20), nullable=False, server_default='0.0')
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    total_price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    
    #review
    review_text = Column(String(500))
    score = Column(DECIMAL(2, 1), CheckConstraint("score >= 1 AND score <= 5", name="valid_score"))
    
    # payment info
    card_info = Column(String(4), nullable=True)  
    transaction_status = Column(
        String(20),
        nullable=False,
        default="Pending"
    )
    payment_type = Column(String(50), nullable=True)  

    order_details = relationship("OrderDetail", back_populates="order")
