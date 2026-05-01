from .client import get_client

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    if order_type == "MARKET":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    elif order_type == "LIMIT":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )