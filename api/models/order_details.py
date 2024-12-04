from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, CheckConstraint, Sequence
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

tracking_number_sequence = Sequence('tracking_number_seq', start=00000, increment=1)

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    
    # customer info
    customer_name = Column(String(100))
    customer_address = Column(String(100))
    customer_email = Column(String(50))
    customer_phone = Column(String(20))
    description = Column(String(300))
    
    # order info
    tracking_number = Column(Integer, tracking_number_sequence, server_default=tracking_number_sequence.next_value(), unique = True)
    order_status = Column(String(20), nullable=False, server_default='0.0')
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    
    #review
    review_text = Column(String(500))
    score = Column(DECIMAL(2, 1), CheckConstraint("score >= 1 AND score <= 5", name="valid_score"))
    
    order = relationship("Order", back_populates="order_details")
