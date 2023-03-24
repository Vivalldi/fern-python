# This file was auto-generated by Fern from our API Definition.

import urllib

import requests


class Client:
    def __init__(self, *, environment: str):
        self._environment = environment

    def test(self) -> None:
        _response = requests.request("GET", urllib.parse.urljoin(f"{self._environment}/", ""))
