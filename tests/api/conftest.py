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
