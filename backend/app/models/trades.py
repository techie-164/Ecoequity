from sqlalchemy import Column, Integer, String
from backend.app.db import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)

    buy_order_id = Column(Integer, ForeignKey("orders.id"))

    sell_order_id = Column(Integer, ForeignKey("orders.id"))

    price = Column(Integer)

    buyer_id = Column(Integer, ForeignKey("users.id"))

    seller_id = Column(Integer, ForeignKey("users.id"))

    quantity = Column(Integer)

    executed_at = Column(DateTime)