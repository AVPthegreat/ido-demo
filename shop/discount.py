"""Discount helpers for the checkout page."""


def apply_discount(price, percent):
    """Return the price after a percent discount (0 to 100)."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return price - price * percent / 100


def best_discount(price, coupons):
    """Return the lowest final price among the given coupon percents."""
    best = price
    for i in range(1, len(coupons)):
        best = min(best, apply_discount(price, coupons[i]))
    return best
