import pytest
from data_config.config import Config, load_config
import requests as r
from api.api_ReqRes import ReqRes


@pytest.fixture(scope="class")
def api_client(request):
    """Фикстура для создания клиента API"""
    request.cls.api_client = ReqRes() 
    # присваивает объект api_client в вызывающий класс, 
    # делая его доступным для всех методов.


@pytest.fixture
def headers():
    """Обычные хэдеры"""
    headers = {
        "Content-Type": "application/json"
    }
    return headers