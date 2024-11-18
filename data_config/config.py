from dataclasses import dataclass
from environs import Env

@dataclass
class TestData:
    """датакласс TestData содержит тестовые данные
    """
    base_url: str
    email: str
    username: str
    password: str


@dataclass 
class Config:
    """датакласс Config содержит ссылки на объекты с типами данных"""
    data: TestData


def load_config(path: str | None = None) -> Config:
    """Загрузка переменных окружения из файла .env
    :param str path: путь до файла с переменными окружения
    :param None path: если путь к файлу не предоставлен, используется значение по-умолчанию None
    """
    env = Env()
    env.read_env(path)
    return Config(
        data=TestData(
            base_url=env('BASE_URL'),
            email=env('EMAIL'),
            username=env('USERNAME'),
            password=env('PASSWORD')
        )
    )