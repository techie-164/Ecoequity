from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.db import get_db
from backend.app.models.trades import Trade

router = APIRouter(
    prefix = "/trade",
    tags = ["Trade"]
)

@router.get("/my-trades")
def my_trades(user_id: int, db: Session = Depends(get_db)):
    trades = db.query(Trade)
    .filter((Trade.buyer_id == user_id) | (Trade.seller_id == user_id))
    .all()
    return trades
