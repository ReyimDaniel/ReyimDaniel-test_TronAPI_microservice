from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from database import SessionLocal, engine, wallet_db_model, WalletRequest
from models import WalletRequestCreate, WalletRequestResponse
from tron import tron_utils

wallet_db_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tron Wallet Info")

# CORS для разрешения запросов с указанного источника
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
get_db - Получение сессии базы данных
Yields:
    Session: активная сессия SQLAlchemy
"""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
create_wallet_info - POST-запрос на получение информации о Tron-кошельке
    Args:
        req (WalletRequestCreate): объект с адресом кошелька из тела запроса
        db (Session, optional): сессия базы данных. Внедряется автоматически
    Raises:
        HTTPException: возникает при некорректном адресе или внутренней ошибке сервера
    Returns:
        WalletRequestResponse: сохраненная запись с информацией о кошельке
"""


@app.post("/wallet_info", response_model=WalletRequestResponse)
def create_wallet_info(req: WalletRequestCreate, db: Session = Depends(get_db)):
    address = req.address.strip()
    print(f"Received address: {address!r}")
    try:
        info = tron_utils.get_wallet_info(address)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

    db_obj = WalletRequest(
        address=req.address,
        balance=info["balance"],
        energy=info["energy"],
        bandwidth=info["bandwidth"]
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


"""
get_wallet_infos - GET-запрос для получения списка записей кошельков с пагинацией
    Args:
        skip (int, optional): количество записей для пропуска
        limit (int, optional): максимальное количество записей для возврата
        db (Session, optional): сессия базы данных
    Returns:
        List[WalletRequestResponse]: список записей с информацией о кошельках
"""


@app.get("/wallet_info", response_model=List[WalletRequestResponse])
def get_wallet_infos(skip: int = 0, limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    return db.query(WalletRequest).order_by(WalletRequest.timestamp.desc()).offset(skip).limit(limit).all()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
