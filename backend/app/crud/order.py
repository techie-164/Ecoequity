from sqlalchemy.orm import Session
from backend.app.services.orderbook import add_order, remove_order
from backend.app.models.orders import Order
from backend.app.schemas.orders import OrderCreate

def create_order(
    db: Session,
    user_id: int,
    order_data: OrderCreate
):
    order = Order(
        user_id=user_id,
        side=order_data.side,
        price=order_data.price,
        quantity=order_data.quantity,
        remaining_quantity=order_data.quantity,
        status="OPEN"
    )

    db.add(order)
    db.commit()
    db.refresh(order)
    add_order(order)

    return order

def get_order_by_id(
    db: Session,
    order_id: int
):
    return (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

def get_user_orders(
    db: Session,
    user_id: int
):
    return (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .all()
    )

def cancel_order(
    db: Session,
    order_id: int
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        return None

    if order.status == "FILLED":
        raise ValueError(
            "Filled orders cannot be cancelled"
        )

    order.status = "CANCELLED"

    db.commit()
    db.refresh(order)
    remove_order(order)

    return order

