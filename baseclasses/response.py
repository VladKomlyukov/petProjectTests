


class Response:
    def assert_status_code_200(status_code: int, response_url: str, response_data: dict) \
        -> None:
        assert status_code == 200, f'FAILURE {response_url}, response: {response_data}'

    def assert_status_code_400(status_code: int):
        assert status_code == 400