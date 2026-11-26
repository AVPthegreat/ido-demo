"""Cart helpers for the checkout page."""


def cart_total(items):
    """Return the total of (price, quantity) pairs in rupees."""
    total = 0
    for price, quantity in items:
        total += price
    return total


def free_delivery(items, threshold=499):
    """Delivery is free when the cart total reaches the threshold."""
    return cart_total(items) > threshold
