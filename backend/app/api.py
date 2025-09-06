from dataclasses import dataclass
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/stocks")
async def read_stocks():
    # Grab data from the DB and have the React server render the stocks pulled from the DB
    # Render Page full of stocks
    return {"message": "Stocks"}
