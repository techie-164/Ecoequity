buy_book = []
sell_book = []

def add_order(order):
    if order.side == 'BUY':
        buy_book.append(order)
    elif order.side == 'SELL':
        sell_book.append(order)
    else:
        raise ValueError("Order side must be 'BUY' or 'SELL'.")

def remove_order(order):
    if order.side == 'BUY':
        buy_book.remove(order)
    elif order.side == 'SELL':
        sell_book.remove(order)
    else:
        raise ValueError("Order side must be 'BUY' or 'SELL'.")