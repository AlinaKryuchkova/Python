import requests, pytest

@pytest.mark.test
class TestCreatePet:
    def test_create_pet(
            self,
            name_category: str = 'dog',
            name_pet: str = 'mick',
            name_tags: str = 'little dog',
            status: str = 'available'
    ):

        response = requests.post(
            url='https://petstore.swagger.io/v2/pet',
            json={
                    "id": 0,
                    "category": {
                        "id": 0,
                        "name": f"{name_category}"
                    },
                    "name": f"{name_pet}",
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                            "id": 0,
                            "name": f"{name_tags}"
                        }
                    ],

                }
        )
        assert response.status_code == 200, f'Не получилось создать пользователя. Response body: {response.text}'

    def test_empty_json(self):

        response = requests.post(
            url='https://petstore.swagger.io/v2/pet',
            headers={'Content-Type': 'application/json'},
            data=''
        )
        assert response.status_code == 405




