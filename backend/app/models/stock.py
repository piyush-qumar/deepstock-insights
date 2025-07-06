from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class StockData(BaseModel):
    ticker: str
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

class Prediction(BaseModel):
    ticker: str
    date: datetime
    prediction: str  # "UP" or "DOWN"
    confidence: Optional[float] = None
