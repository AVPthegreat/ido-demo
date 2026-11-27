"""Shipping fee helpers for the checkout page."""

FREE_DELIVERY_FROM = 499  # rupees; orders at or above this ship free
BASE_FEE = 40
PER_KG_FEE = 15


def shipping_fee(cart_total, weight_kg):
    """Return the delivery fee in rupees for a cart.

    Orders of FREE_DELIVERY_FROM or more ship free. Otherwise the fee is
    BASE_FEE plus PER_KG_FEE for every started kilogram after the first.
    """
    if cart_total < 0 or weight_kg < 0:
        raise ValueError("cart_total and weight_kg must not be negative")
    if cart_total >= FREE_DELIVERY_FROM:
        return 0
    extra_kg = max(0, -(-weight_kg // 1) - 1)  # started kilograms after the first
    return BASE_FEE + PER_KG_FEE * int(extra_kg)
