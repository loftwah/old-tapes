import os
from typing import Optional
import requests

def initialize_client():
    access_token = os.environ["ACCESS_TOKEN"]
    return GraphAPIClient(access_token)


class GraphAPIClient:
    URL = "https://graph.facebook.com/v6.0/"

    def __init__(self, access_token: str):
        self.access_token = access_token

    def get_user_data(self, user_id: Optional[str]=None):
        if user_id is None:
            user_id = os.environ["USER_ID"]
        url = f"{self.URL}/{user_id}/"
        return requests.get(url, params={"access_token": self.access_token})
