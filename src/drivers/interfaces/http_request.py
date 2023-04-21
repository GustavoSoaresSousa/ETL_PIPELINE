from typing import Dict
from abc import ABC, abstractmethod

class HttpRequesterInterface(ABC):

  @abstractmethod
  def request_from_page(self) -> Dict[int, str]:
    pass