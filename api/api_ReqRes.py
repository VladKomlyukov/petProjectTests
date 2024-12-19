import requests as r
from data_config.config import Config, load_config
import json


class ReqRes:
    """API запросы ReqRes
    """
    def __init__(self) -> None:
        config: Config = load_config()
        self.base_url: str = config.data.base_url
        self.username: str = config.data.username
        self.password: str = config.data.password
        self.email: str = config.data.email
        
    
    def post_registration(self, username, password, email, headers: dict) -> tuple:
        """Регистрация пользователя
        Args:
            username (_type_): имя пользователя
            password (_type_): пароль
            email (_type_): эл. почта
            headers (dict): заголовки запроса
        Returns:
            tuple: статус код, ответ на запрос
        """
        data = json.dumps({
            "username": username,
            "email": email,
            "password": password
        })
        response = r.post(url=self.base_url + '/register', headers=headers, data=data)
        return response.status_code, response.json(), response.url


    def get_all_users(self, headers: dict) -> tuple:
        """Получение информации о всех пользователях
        Args:
            headers (dict): заголовки для запроса
        Returns:
            tuple: статус код, ответ на запрос
        """
        response = r.get(url=self.base_url + '/users', headers=headers)
        return response.status_code, response.json(), response.url
    
    def get_user_by_id(self, headers: dict, ids: str) -> tuple:
        """Получение информации о пользователе по его id
        Args:
            headers (dict): заголовки для запроса
            ids (str): id запрашиваемого пользователя
        Returns:
            tuple: статус код, ответ на запрос
        """    
        response = r.get(url=self.base_url + f'/users/{ids}', headers=headers)
        return response.status_code, response.json(), response.url
    
    def get_resources(self, headers:dict) -> tuple:
        """Получение информации о всех ресурсах на сервере
        Args:
            headers (dict): заголовки для запроса
        Returns:
            tuple: статус код, ответ на запрос
        """
        response = r.get(url=self.base_url + '/resource', headers=headers)
        return response.status_code, response.json(), response.url
    
    def get_resource_by_id(self, headers: dict, ids: str) -> tuple:
        """Получение информации о ресурсе по его id
        Args:
            headers (dict): заголовки для запроса
        Returns:
            tuple: статус код, ответ на запрос
        """
        response = r.get(url=self.base_url + f'/resource/{ids}', headers=headers)
        return response.status_code, response.json(), response.url

    def post_login(self, headers: dict, data) -> tuple:
        """Авторизация пользователя по логину и паролю
        Args:
           headers (dict): заголовки для запроса
        Returns:
            tuple: статус код, ответ на запрос
        """
        data = json.dumps(data)
        response = r.post(url=self.base_url + '/login', headers=headers, data=data)
        return response.status_code, response.json(), response.url
    
