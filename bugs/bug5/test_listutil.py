from listutil import largest, smallest, spread

def test_largest():
    assert largest([3, 1, 2]) == 3

def test_smallest():
    assert smallest([3, 1, 2]) == 1

def test_spread():
    assert spread([3, 1, 2]) == 2

def test_spread_equal():
    assert spread([5, 5]) == 0
    