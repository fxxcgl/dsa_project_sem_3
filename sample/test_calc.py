from calc import add, multiply, average, describe

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 3) == 6

def test_average():
    assert average([2, 4]) == 3

def test_describe():
    assert describe([2, 4]) == (3, 4)