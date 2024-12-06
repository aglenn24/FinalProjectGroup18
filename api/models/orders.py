from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, CheckConstraint, Sequence
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

tracking_number_sequence = Sequence('tracking_number_seq', start=00000, increment=1)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey('sandwiches.id'), nullable=False)
    promo_code_id = Column(Integer, ForeignKey('promo_codes.id'), nullable=True)

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
    
    # payment info
    card_info = Column(String(25), nullable=True)  
    transaction_status = Column(
        String(20),
        nullable=False,
        default="Pending"
    )
    
    total_price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    
    payment_type = Column(String(50), nullable=True)  
    
    order_details = relationship("OrderDetail", back_populates="orders")
    sandwiches = relationship("Sandwich", back_populates="orders")
    promo_code = relationship("PromoCodes", back_populates="orders")