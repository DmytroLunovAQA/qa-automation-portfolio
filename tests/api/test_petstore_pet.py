import pytest
from config.config import Config


class TestPetEndpoints:

    def test_get_pet_by_id_positive(self, petstore_api):
        pet_id = 1

        response = petstore_api.get(f"/pet/{pet_id}")
        assert (
            response.status_code == 200
        ), f"Expected status code is 200, actual is {response.status_code}"

        data = response.json()
        assert "id" in data, "Response doesn't have 'id' key"
        assert "name" in data, "Response doesn't have 'name' key"
        assert (
            data["id"] == pet_id
        ), f"ID don't correspond, expected id was: {pet_id}, actual ID is: {data["id"]}"

        print(f"Pet is found: {data.get('name')} (ID: {data.get("id")})")

    def test_get_pet_by_id_negative(self, petstore_api):
        pet_id = 99999999
        response = petstore_api.get(f"/pet/{pet_id}")
        assert (
            response.status_code == 404
        ), f"Expected status code is 404, actual is {response.status_code}"

        print(f"Pet ID {pet_id} not found (Expected Result)")
