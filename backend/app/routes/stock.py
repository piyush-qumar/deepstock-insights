from fastapi import APIRouter, HTTPException
from app.models.stock import StockData, Prediction
from app.db import db

router = APIRouter()

@router.post("/stock", tags=["Stock"])
async def save_stock_data(stock: StockData):
    await db["stock_data"].insert_one(stock.dict())
    return {"message": "Stock data saved"}

@router.get("/stock/{ticker}", tags=["Stock"])
async def get_stock_data(ticker: str):
    data = db["stock_data"].find({"ticker": ticker})
    return [doc async for doc in data]

@router.post("/predict", tags=["Prediction"])
async def save_prediction(pred: Prediction):
    await db["predictions"].insert_one(pred.dict())
    return {"message": "Prediction saved"}

@router.get("/predict/{ticker}", tags=["Prediction"])
async def get_prediction(ticker: str):
    data = db["predictions"].find({"ticker": ticker})
    return [doc async for doc in data]
