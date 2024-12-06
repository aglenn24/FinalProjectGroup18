from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from ..dependencies.database import Base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')
    # menu_id = Column(Integer, ForeignKey("menus.id"))

    sandwiches = relationship("Sandwich", back_populates="recipe")
    resources = relationship("Resource", back_populates="recipe")
    # menu = relationship("Menu", back_populates="recipes")