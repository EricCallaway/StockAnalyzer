from fastapi import APIRouter
from app.models.stock import Stock

import logging

_logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/stocks",
    tags=['stocks']
)

fake_stock_data = {
    "NVDA": "Nvidia",
    "MSFT": "Microsoft",
    "AAPL": "Apple",
    "GOOG": "Alphabet",
    "AMZN": "Amazon"
}

@router.get('/')
async def read_stocks():
    return fake_stock_data

@router.get('/{ticker_symbol}')
async def read_stock(ticker_symbol: str):
    if ticker_symbol in fake_stock_data:
        return fake_stock_data[ticker_symbol.upper()]
    return "Stock not in database"

@router.post('/')
async def create_stock(stock: Stock):
    # Validate input against some stock model
    _logger.info(f"Creating Entry in stock table: Ticker: {stock.ticker}, Name: {stock.name}")
    # Create record in the DB
    new_stock = {stock.ticker: stock.name}
    fake_stock_data.update(new_stock)
