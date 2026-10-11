def apply_discount(price, percent):
    return price - price * percent / 10

def cart_total(prices, percent):
    total = 0
    for p in prices:
        total += apply_discount(p, percent)
    return total

def checkout(prices, percent):
    return round(cart_total(prices, percent), 2)