from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

"""
Модель для создания таблицы БД
    __tablename__ (str): название таблицы в БД
    id (int): уникальный идентификатор записи
    address (str): URL Tron-кошелька
    balance (float): баланс TRX на кошельке
    energy (int): количество оставшейся энергии
    bandwidth (int): количество оставшейся пропускной способности
    timestamp (datetime): время создания записи
"""


class WalletRequest(Base):
    __tablename__ = "wallet_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    balance = Column(Float)
    energy = Column(Integer)
    bandwidth = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
