import requests, pytest

@pytest.mark.test
class TestDeletePet:
    def test_delete_pet(
            self,
            pet_id: int = 2
    ):
        response = requests.delete(url = f'https://petstore.swagger.io/v2/pet/{pet_id}')
        assert  response.status_code == 200, f'Не получилось удалить питомца. Response body: {response.text}'

    def test_invalid_id(
            self,
            pet_id: int = 1.1
    ):
        response = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{pet_id}')
        assert response.status_code == 404

    def test_pet_not_found(
            self,
            pet_id: int = 1500000
    ):
        response = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{pet_id}')
        assert response.status_code == 404