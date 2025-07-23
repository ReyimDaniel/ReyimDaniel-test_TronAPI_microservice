from datetime import datetime
from pydantic import BaseModel

"""
WalletRequestCreate - Модель для POST-запроса для получение информации о Tron-кошельке
    address (str): Tron-адрес кошелька.
"""


class WalletRequestCreate(BaseModel):
    address: str


"""
WalletRequestResponse - Модель для использования таблицы БД запросом
     __tablename__ (str): название таблицы в базе данных
    id (int): уникальный идентификатор записи (первичный ключ)
    address (str): адрес Tron-кошелька
    balance (float): баланс TRX на кошельке
    energy (int): количество оставшейся энергии
    bandwidth (int): количество оставшейся пропускной способности 
    timestamp (datetime): время создания записи
"""


class WalletRequestResponse(BaseModel):
    id: int
    address: str
    balance: float
    energy: int
    bandwidth: int
    timestamp: datetime

    class Config:
        orm_mode = True
