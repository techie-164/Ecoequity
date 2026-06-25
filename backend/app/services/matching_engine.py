from sqlalchemy.orm import Session

from backend.app.models.orders import Order
from backend.app.models.trades import Trade
from backend.app.models.users import User

from backend.app.services.orderbook import (
    buy_book,
    sell_book,
    add_order,
    remove_order
)


def match(order: Order, db: Session):

    if order.side == "BUY":
        match_buy(order, db)
    else:
        match_sell(order, db)


def match_buy(order: Order, db: Session):

    buyer = db.query(User).filter(User.id == order.user_id).first()

    while order.remaining_quantity > 0 and sell_book:

        seller_order = sell_book[0]

        if seller_order.price > order.price:
            break

        seller = db.query(User).filter(
            User.id == seller_order.user_id
        ).first()

        matched_quantity = min(
            order.remaining_quantity,
            seller_order.remaining_quantity
        )

        total_cost = matched_quantity * seller_order.price

        if buyer.carbon_coins < total_cost:
            break

        if seller.carbon_balance < matched_quantity:
            break

        buyer.carbon_coins -= total_cost
        buyer.carbon_balance += matched_quantity

        seller.carbon_coins += total_cost
        seller.carbon_balance -= matched_quantity

        order.remaining_quantity -= matched_quantity
        seller_order.remaining_quantity -= matched_quantity

        trade = Trade(
            buy_order_id=order.id,
            sell_order_id=seller_order.id,
            buyer_id=buyer.id,
            seller_id=seller.id,
            quantity=matched_quantity,
            price=seller_order.price
        )

        db.add(trade)

        if seller_order.remaining_quantity == 0:
            seller_order.status = "FILLED"
            remove_order(seller_order)
        else:
            seller_order.status = "PARTIALLY_FILLED"

    if order.remaining_quantity == 0:
        order.status = "FILLED"
    else:
        order.status = "PARTIALLY_FILLED"
        add_order(order)

    db.commit()


def match_sell(order: Order, db: Session):

    seller = db.query(User).filter(User.id == order.user_id).first()

    while order.remaining_quantity > 0 and buy_book:

        buyer_order = buy_book[0]

        if buyer_order.price < order.price:
            break

        buyer = db.query(User).filter(
            User.id == buyer_order.user_id
        ).first()

        matched_quantity = min(
            order.remaining_quantity,
            buyer_order.remaining_quantity
        )

        total_cost = matched_quantity * order.price

        if buyer.carbon_coins < total_cost:
            break

        if seller.carbon_balance < matched_quantity:
            break

        buyer.carbon_coins -= total_cost
        buyer.carbon_balance += matched_quantity

        seller.carbon_coins += total_cost
        seller.carbon_balance -= matched_quantity

        order.remaining_quantity -= matched_quantity
        buyer_order.remaining_quantity -= matched_quantity

        trade = Trade(
            buy_order_id=buyer_order.id,
            sell_order_id=order.id,
            buyer_id=buyer.id,
            seller_id=seller.id,
            quantity=matched_quantity,
            price=order.price
        )

        db.add(trade)

        if buyer_order.remaining_quantity == 0:
            buyer_order.status = "FILLED"
            remove_order(buyer_order)
        else:
            buyer_order.status = "PARTIALLY_FILLED"

    if order.remaining_quantity == 0:
        order.status = "FILLED"
    else:
        order.status = "PARTIALLY_FILLED"
        add_order(order)

    db.commit()