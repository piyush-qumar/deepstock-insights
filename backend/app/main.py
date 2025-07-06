from fastapi import FastAPI
from app.routes import stock

app = FastAPI()

app.include_router(stock.router)

@app.get("/")
def read_root():
    return {"msg": "DeepStock ML Backend is Live"}
