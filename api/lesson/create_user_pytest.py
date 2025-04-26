import requests, pytest

@pytest.mark.test
class TestCreateUser:
    def test_create_user(
            self,
            user_name: str = 'python_babies',
            first_name: str = 'nobugs',
            last_name: str = 'deafult',
            password: str = 'qwerty'
    ):
        response = requests.post(
            url='https://petstore.swagger.io/v2/user/',
            json={
                "id": 0,
                "username": f"{user_name}",
                "firstName": f"{first_name}",
                "lastName": f"{last_name}",
                "email": "string",
                "password": f"{password}",
                "phone": "string",
                "userStatus": 0
            }
        )
        assert response.status_code == 200, f'Не получилось создать пользователя. Response body: {response.text}'

    def test_get_user(
            self,
            user_name: str = 'python_babies'
    ):
        response = requests.get(url=f'https://petstore.swagger.io/v2/user/{user_name}')
        assert response.status_code == 200, 'Нет такого пользователя'

    def test_delete_user(
            self,
            user_name: str = 'python_babies'
    ):
        response = requests.delete(url=f'https://petstore.swagger.io/v2/user/{user_name}')
        assert response.status_code == 200, 'Не получилось удалить пользователя'

