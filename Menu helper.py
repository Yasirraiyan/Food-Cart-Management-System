

menu = ["pizza", "pazta", "coffee", "biriyani", "burger"]
prices = {
    "pizza": 40,
    "pazta": 50,
    "coffee": 60,
    "biriyani": 70,
    "burger": 80
}

def is_valid_choice(choice):
    """Check if the chosen item is in the menu."""
    return choice in menu

def get_price(choice):
    """Return the price of the chosen item."""
    return prices.get(choice, 0)
