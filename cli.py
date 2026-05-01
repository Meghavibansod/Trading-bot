import click
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger
import logging

setup_logger()

@click.command()
@click.option('--symbol', required=True)
@click.option('--side', required=True)
@click.option('--order_type', required=True)
@click.option('--quantity', required=True, type=float)
@click.option('--price', required=False, type=float)
def run(symbol, side, order_type, quantity, price):
    try:
        validate_side(side)
        validate_order_type(order_type)
        validate_price(order_type, price)
        validate_quantity(quantity)

        
        #    ORDER REQUEST
        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")
        if price:
            print(f"Price      : {price}")

        print("\nPlacing order...\n")

        logging.info(f"Request: {symbol}, {side}, {order_type}, {quantity}, {price}")

        # API CALL
        response = place_order(symbol, side, order_type, quantity, price)

        #  ORDER RESPONSE
        print("========== ORDER RESPONSE ==========")
        print(f"Order ID        : {response.get('orderId')}")
        print(f"Status          : {response.get('status')}")
        print(f"Executed Qty    : {response.get('executedQty')}")
        print(f"Avg Price       : {response.get('avgPrice', 'N/A')}")

        print("\n Order placed successfully!")

        logging.info(f"Response: {response}")

    except Exception as e:
        print("\n Order failed!")
        print(f"Reason: {e}")
        logging.error(str(e))


if __name__ == "__main__":
    run()