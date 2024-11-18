import pytest
from api.api_ReqRes import ReqRes
from baseclasses.response import Response as response
from baseclasses import data



@pytest.mark.usefixtures('api_client')
class TestReqRes():
    api_client: ReqRes # Явное указание типа, чтобы IDE дополняла методы классов

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_post_registration_positive(self, headers):
        username, password = data.uspass_gen()
        email = data.email_gen()
        status_code, response_data, response_url = self.api_client.post_registration(username, password, email, headers=headers)
        response.assert_status_code_success(status_code, response_data, response_url)
        #response.assert_status_code_400

    def test_get_all_users(self, headers):
        status_code, response_data, response_url = self.api_client.get_all_users(headers=headers)
        response.assert_status_code_200(status_code, response_url, response_data)
        assert len(response_data['data']) == 6, 'Length of data list is not 6'
    
    @pytest.mark.parametrize('ids', ['1', '2', '3', '4', '5', '6'])
    def test_get_user_by_id(self, headers, ids):
         status_code, response_data, response_url = self.api_client.get_user_by_id(headers=headers, ids=ids)
         response.assert_status_code_200(status_code, response_url, response_data)

    def test_get_resourses(self, headers):
        status_code, response_data, response_url = self.api_client.get_resources(headers=headers)
        response.assert_status_code_200(status_code, response_url, response_data)


    @pytest.mark.parametrize('ids', ['1', '2', '3', '4', '5', '6'])
    def test_resource_by_id(self, headers, ids):
        status_code, response_data, response_url = self.api_client.get_resource_by_id(headers=headers, ids=ids)
        response.assert_status_code_200(status_code, response_url, response_data)
        
    
    @pytest.mark.parametrize('data', [
        {"username":"hello321", "email":"test1313@rambler.ru", "password":"qwerty321"}, 
        {"username":"hello654", "email":"test1414@rambler.ru", "password":"qwerty321"}, 
        {"username":"hello987", "email":"test1515@rambler.ru", "password":"qwerty321"}
        ])
    def test_post_login(self, headers, data):
        status_code, response_data, response_url = self.api_client.post_login(headers=headers, data=data)
        response.assert_status_code_400(status_code)