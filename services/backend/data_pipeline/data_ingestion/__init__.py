from abc import ABC, ABCMeta, abstractmethod
from enum import Enum
from typing import Dict, Any, Optional

class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class APIInterface(ABC):

    @abstractmethod
    def request(self,
        method: HTTPMethod,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """This method is used to make HTTP requests with the specified method"""
        pass


    def get(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        return self.request(HTTPMethod.GET, endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        return self.request(HTTPMethod.POST, endpoint, **kwargs)
