from fastapi import APIRouter
from app.models.stock import Stock
from data_pipeline.data_ingestion.integrations.alpha_advantage.api_alpha_advantage import AlphaAdvantageInterface

import logging

_logger = logging.getLogger("uvicorn")

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
    _logger.info("Reading demo stock data")
    return fake_stock_data

@router.get('/{ticker_symbol}')
async def read_stock(ticker_symbol: str):
    if ticker_symbol in fake_stock_data:
        return fake_stock_data[ticker_symbol.upper()]
    return "Stock not in database"

@router.get('/alpha/{ticker_symbol}')
async def read_aplpha_stock(ticker_symbol: str):
    alpha_advantage = AlphaAdvantageInterface()
    data = alpha_advantage.core_stock_time_series_daily()
    return data

@router.post('/')
async def create_stock(stock: Stock):
    # Validate input against some stock model
    _logger.info(f"Creating Entry in stock table: Ticker: {stock.ticker}, Name: {stock.name}")
    # Create record in the DB
    new_stock = {stock.ticker: stock.name}
    fake_stock_data.update(new_stock)
