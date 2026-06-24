from sqlalchemy import Column, Integer, String
from backend.app.db import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    side = Column(String, nullable=False)  

    price = Column(Integer, nullable=False)

    quantity = Column(Integer, nullable=False)

    remaining_quantity = Column(Integer, nullable=False)

    status = Column(String, nullable=False)

    created_at = Column(DateTime)