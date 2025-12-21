"""
This are fixtures for API tests
"""

import pytest
from config.config import Config
from utils.api_client import APIClient


@pytest.fixture
def petstore_api():
    """
    Fixture: API Client for Petstore tests
    It is separately created for each test that runs
    """
    api = APIClient(Config.PETSTORE_BASE_URL)
    yield api
    api.close()


@pytest.fixture
def create_test_pet(petstore_api):
    """
    Fixture: Creates a text pet and deletes it after the test
    """
    pet_data = {
        "id": 12345,
        "name": "Test Dog",
        "status": "available",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "test"}],
    }

    response = petstore_api.post("/pet", data=pet_data)
    created_pet = response.json() if response.status_code == 200 else pet_data

    yield created_pet  # return created pet into test

    # Teardown: delete pet after test
    try:
        petstore_api.delete(f"/pet/{created_pet['id']}")
    except Exception as e:
        print(f"Can't delete a pet: {e}")
