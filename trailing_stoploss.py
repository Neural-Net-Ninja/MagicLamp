def trailing_stop_loss(price, highest_price, stop_percent):
    """
    Check if a trailing stop loss order would be triggered.

    Parameters:
    price (float): The current price of the stock.
    highest_price (float): The highest price the stock has reached since it was bought.
    stop_percent (float): The trailing stop percentage. For example, 0.05 for a 5% trailing stop.

    Returns:
    bool: True if the order would be triggered, False otherwise.
    """
    # Calculate the stop price based on the highest price
    stop_price = highest_price * (1 - stop_percent)
    
    if price < stop_price:
        return True
    else:
        return False


# Example usage:
price = 96
highest_price = 100
stop_percent = 0.03
if trailing_stop_loss(price, highest_price, stop_percent):
    print("Stop loss order triggered!")
