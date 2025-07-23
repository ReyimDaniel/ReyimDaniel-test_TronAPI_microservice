from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base


class WalletRequest(Base):
    __tablename__ = "wallet_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    balance = Column(Float)
    energy = Column(Integer)
    bandwidth = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
