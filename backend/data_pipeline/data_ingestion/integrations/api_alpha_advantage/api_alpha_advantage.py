import requests

from abc import ABC, abstractmethod

class AlphaAdvantageInterface(ABC):
    @abstractmethod
    def _make_request(self):
        pass
