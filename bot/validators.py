def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

def validate_price(order_type, price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")
    
def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")