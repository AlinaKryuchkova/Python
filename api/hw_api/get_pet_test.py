from http.client import responses

import requests, pytest

@pytest.mark.test
class TestGetPet:
    def test_get_pet(
            self,
            pet_id: int = 1
    ):
        response = requests.get(url = f'https://petstore.swagger.io/v2/pet/{pet_id}')
        assert  response.status_code == 200, f'Нет такого питомца. Response body: {response.text}'

    def test_invalid_id(
            self,
            pet_id: int = 1.1
    ):
        response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}')
        assert response.status_code == 404

    def test_pet_not_found(
            self,
            pet_id: int = 1500000
    ):
        response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}')
        assert response.status_code == 404
