import requests
from typing import Dict
from .interfaces.http_request import HttpRequesterInterface

class HttpRequester(HttpRequesterInterface):
  def __init__(self) -> None:
    self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

  def request_from_page(self):
    response = requests.get(self.__url)
    return {
      "status_code": response.status_code,
      "html": response.text
    }
    