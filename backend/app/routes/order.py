from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.db import get_db
from backend.app.crud.order import create_order, get_order_by_id, get_user_orders, cancel_order
from backend.app.schemas.order import OrderCreate, OrderResponse

router = APIRouter(
    prefix = "/order",
    tags = ["Order"]
)

@router.post("/create", response_model = OrderResponse)
def create_order_route(
    order_data: OrderCreate, 
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)):
    new_order = create_order(db,current_user.id,order_data)
    return new_order

@router.delete("/delete")
def cancel_order_route(
    order_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    cancel_order(db, order_id)
    return {"message": "Order cancelled successfully"}

@router.get("/my-orders")
def my_orders(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_user_orders(
        db,
        current_user.id
    )

@router.get("/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    return get_order_by_id(
        db,
        order_id
    )
    