import pytest

from shop.shipping import shipping_fee


def test_free_at_threshold():
    assert shipping_fee(499, 3) == 0


def test_first_kilogram_is_base_fee():
    assert shipping_fee(100, 0.4) == 40
    assert shipping_fee(100, 1) == 40


def test_started_kilograms_are_charged():
    assert shipping_fee(100, 1.2) == 55
    assert shipping_fee(100, 3) == 70


def test_empty_cart_weight_zero():
    assert shipping_fee(0, 0) == 40


def test_negative_input_rejected():
    with pytest.raises(ValueError):
        shipping_fee(-1, 1)
