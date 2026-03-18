API_KEY = "api_key"
API_SECRET = "api_secret"
import argparse
import logging

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

def prompt_if_none(value, prompt, default=None):
    if value:
        return value
    user_input = input(f"{prompt} [{default}]: ")
    return user_input.strip() if user_input else default


def main():
    setup_logger()

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity")
    parser.add_argument("--price")

    args = parser.parse_args()

    symbol = prompt_if_none(args.symbol, "Enter Symbol", "BTCUSDT")
    side = prompt_if_none(args.side, "Enter Side (BUY/SELL)", "BUY").upper()
    order_type = prompt_if_none(args.type, "Enter Order Type (MARKET/LIMIT)", "MARKET").upper()
    quantity = prompt_if_none(args.quantity, "Enter Quantity", "0.002")
    price = args.price

    if order_type == "LIMIT":
        price = prompt_if_none(price, "Enter Price", "77774.76")

    try:
        side, order_type, quantity, price = validate_order(symbol,side,order_type,quantity,price)

        client = BinanceClient(API_KEY, API_SECRET).get_client()

        print("\n ORDER REQUEST")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        order = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n ORDER RESPONSE")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")

        print("\n ORDER SUCCESS")

    except Exception as e:
        print("\n ORDER FAILED")
        print(str(e))
        logging.error(str(e))

if __name__ == "__main__":
    main()
