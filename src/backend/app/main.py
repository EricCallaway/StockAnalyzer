from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .routers import stocks

app = FastAPI()
app.include_router(stocks.router)


@app.get("/")
async def read_root():
    # render a home page
    return {"page": "Home Page"}

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')
