import requests
from abc import ABC, abstractmethod
from data_pipeline.data_ingestion import APIInterface, HTTPMethod
from typing import Optional, Dict, Any
import os

import logging

_logger = logging.getLogger("uvicorn")

class AlphaAdvantageInterface(APIInterface):
    def request(self,
        method: HTTPMethod,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """This method is used to make HTTP requests with the specified method"""
        result = getattr(requests, method)()
        _logger.info(f"Making Request from AlphaAdvantageInterface with data: {result}")
        return result

    def core_stock_time_series_daily(self) -> dict:
        api_key = os.getenv('API_KEY_ALPHA_ADVANTAGE')
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={api_key}'
        result = requests.get(url)
        data = result.json()

        _logger.info("Processing Data from core_stock_time_series_daily")
        return data
