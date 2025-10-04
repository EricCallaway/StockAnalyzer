FROM python:3.10-slim

WORKDIR /dbt_stock_analyzer

RUN pip install --no-cache-dir dbt-postgres

COPY . .

CMD ["dbt", "run"]
