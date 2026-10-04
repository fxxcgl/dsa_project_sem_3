from mathutil import square, cube, sum_squares

def test_square_pos():
    assert square(3) == 9

def test_square_neg():
    assert square(-3) == 9

def test_cube():
    assert cube(2) == 8

def test_sum_squares():
    assert sum_squares([1, 2]) == 5

def test_sum_squares_neg():
    assert sum_squares([-1, 2]) == 5