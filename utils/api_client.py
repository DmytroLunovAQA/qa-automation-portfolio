import requests
from config.config import Config
from typing import Optional, Dict, Any


class APIClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {"Content-Type": "application/json", "Accept": "application/json"}
        )

    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        """
        Get request

        :param endpoint: Endpoint (i.e. '/pet/1')
        :param params: Query parameters
        :return: Response object
        """

        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=Config.API_TIMEOUT)
        return response

    def post(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """
        Post request

        :param endpoint: Endpoint
        :param data: JSON data to post
        :return: Response object
        """

        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data, timeout=Config.API_TIMEOUT)
        return response

    def put(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """
        Put request

        :param endpoint: Endpoint
        :param data: JSON data to post
        :return: Response object
        """

        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data, timeout=Config.API_TIMEOUT)
        return response

    def delete(self, endpoint: str) -> requests.Response:
        """
        Delete request

        :param endpoint: Endpoint
        :return: DescriptionResponse object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, timeout=Config.API_TIMEOUT)
        return response

    def close(self):
        self.session.close()
