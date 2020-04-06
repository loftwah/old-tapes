import os
from typing import Optional, Tuple
import requests
from requests import Response

from old_tapes.exceptions import BadResponse


def initialize_client():
    access_token = os.environ["ACCESS_TOKEN"]
    return GraphAPIClient(access_token)


class GraphAPIClient:
    URL = "https://graph.facebook.com/v6.0/"

    def __init__(self, access_token: str):
        self.access_token = access_token

    def get(self, url: str) -> Tuple[list, Optional[str]]:
        response = requests.get(url)
        return self.process_response(response)

    def get_user_posts(
        self, user_id: Optional[str] = None
    ) -> Tuple[list, Optional[str]]:
        if user_id is None:
            user_id = "me"
        url = f"{self.URL}{user_id}/posts/"
        response = requests.get(
            url,
            params={
                "access_token": self.access_token,
                "fields": "id,link,created_time,name",
            },
        )
        return self.process_response(response)

    def process_response(self, response: Response) -> Tuple[list, Optional[str]]:
        if not response.status_code == 200:
            raise BadResponse(response.json())

        data = response.json()
        return data.get("data"), data.get("paging", {"next": None}).get("next")
