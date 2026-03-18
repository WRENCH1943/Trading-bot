import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(
            f"Request -> symbol={symbol}, side={side}, type={order_type}, qty={quantity}, price={price}"
        )

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Response -> {response}")

        return response

    except Exception as e:
        logging.error(f"Order Error -> {str(e)}")
        raise Exception(f"Order failed: {str(e)}")