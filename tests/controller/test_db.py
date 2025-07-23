from sqlalchemy.orm import Session

from database import SessionLocal, wallet_db_model

"""
    Тест записи и чтения записи в БД
    Проверяет что:
    1) запись успешно добавлена и найдена по адресу
    2) значение баланса совпадает с ожидаемым
"""


def test_create_wallet_in_db():
    db: Session = SessionLocal()
    test_data = wallet_db_model.WalletRequest(
        address="test_address",
        balance=100.0,
        energy=2000,
        bandwidth=5000
    )
    db.add(test_data)
    db.commit()

    result = db.query(wallet_db_model.WalletRequest).filter_by(address="test_address").first()
    assert result is not None
    assert result.balance == 100.0
    db.delete(result)
    db.commit()
    db.close()
