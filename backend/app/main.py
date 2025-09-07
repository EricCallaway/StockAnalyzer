from fastapi import FastAPI
from .routers import stocks

app = FastAPI()
app.include_router(stocks.router)

@app.get("/")
async def read_root():
    # render a home page
    return {"page": "Home Page"}
