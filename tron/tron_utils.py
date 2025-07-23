import traceback
from tronpy import Tron
from tronpy.exceptions import AddressNotFound

client = Tron()

"""
    Получение информации о Tron-кошельке - баланс, энергия и пропускную способность
    Args:
        address (str): Tron-адрес кошелька
    Returns:
        dict: Словарь с ключами:
            - "balance" (float): баланс TRX
            - "energy" (int): оставшаяся энергия кошелька
            - "bandwidth" (int): оставшаяся пропускная способность
    Raises:
        ValueError: если адрес не найден в блокчейне или произошла другая ошибка при запросе

"""


def get_wallet_info(address: str) -> dict:
    try:
        account = client.get_account(address)
        balance = account.get('balance', 0) / 1_000_000
        resources = client.get_account_resource(address)
        energy = resources.get('EnergyRemaining', 0)
        bandwidth = resources.get('FreeNetRemaining', 0)
        return {"balance": balance, "energy": energy, "bandwidth": bandwidth}
    except AddressNotFound:
        raise ValueError("Invalid Tron address")
    except Exception as e:
        raise ValueError("Failed to get wallet info")
