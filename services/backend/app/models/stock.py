from pydantic import BaseModel


class Stock(BaseModel):
    id: int
    name: str
    ticker: str
    current_price: float
    market_capitalization: float
    price_to_earnings: float
    earnings_per_share: float
    dividend_yield: float
    ticker: str
    name: str
