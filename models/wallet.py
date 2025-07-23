from datetime import datetime
from pydantic import BaseModel


class WalletRequestCreate(BaseModel):
    address: str


class WalletRequestResponse(BaseModel):
    id: int
    address: str
    balance: float
    energy: int
    bandwidth: int
    timestamp: datetime

    class Config:
        orm_mode = True
