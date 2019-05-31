import requests
from bs4 import BeautifulSoup

from . import errors


def get_soup_from_url(url: str) -> BeautifulSoup:
    response = requests.get(url)

    if response.status_code != 200:
        raise errors.HttpResponseError(url, response.status_code)

    return BeautifulSoup(response.text, "html.parser")
