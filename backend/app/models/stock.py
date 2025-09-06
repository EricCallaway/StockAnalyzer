from dataclasses import dataclass

@dataclass
class Stock:
    name: str
    ticker: str
    current_price: float
