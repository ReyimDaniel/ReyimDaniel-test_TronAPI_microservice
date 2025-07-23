from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

"""
   test_post_invalid - Тестирует POST-запрос к эндпоинту /wallet_info с неправильным адресом
   Проверяет, что при отправке неправильного Tron-адреса возвращается HTTP-статус 400 Bad Request
"""


def test_post_invalid():
    response = client.post("/wallet_info", json={"address": "invalid"})
    assert response.status_code == 400


"""
    test_get_wallets - Тестирует GET-запрос к эндпоинту /wallet_info для получения списка записей
    Проверяет, что запрос проходит успешно и возвращается список
"""


def test_get_wallets():
    response = client.get("/wallet_info")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
