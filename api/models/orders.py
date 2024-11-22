from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    customer_address = Column(String(100))
    customer_email = Column(String(50))
    customer_phone = Column(String(20))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    tracking_number = Column(Integer)
    order_status = Column(String(20))
    total_price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    order_details = relationship("OrderDetail", back_populates="order")
