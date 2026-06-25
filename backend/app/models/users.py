from sqlalchemy import Column, Integer, String

from backend.app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    role = Column(String, nullable=False)

    carbon_coins = Column(Integer, nullable=False)

    carbon_balance = Column(Integer, default=0)

    emission_limit = Column(Integer)

    current_emission = Column(Integer)