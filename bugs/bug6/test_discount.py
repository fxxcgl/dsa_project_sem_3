from discount import apply_discount, cart_total, checkout

def test_no_discount():
    assert apply_discount(100, 0) == 100

def test_zero_price():
    assert apply_discount(0, 20) == 0

def test_apply_discount():
    assert apply_discount(200, 10) == 180

def test_cart_total():
    assert cart_total([100, 50], 10) == 135

def test_checkout():
    assert checkout([100], 20) == 80