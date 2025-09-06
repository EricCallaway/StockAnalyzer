create table stock (    id INTEGER PRIMARY KEY,
    current_price FLOAT,
    market_capitalization FLOAT,
    price_to_earnings FLOAT,
    earnings_per_share FLOAT,
    dividend_yield FLOAT,
    ticker VARCHAR,
    name VARCHAR
);

create INDEX idx_stock_ticker on stock(ticker);