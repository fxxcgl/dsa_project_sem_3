from grades import letter, report, passed

def test_letter_a():
    assert letter(95) == "A"

def test_letter_b():
    assert letter(85) == "B"

def test_letter_c():
    assert letter(75) == "C"

def test_letter_boundary():
    assert letter(70) == "C"

def test_report():
    assert report([95, 85]) == "A,B"

def test_passed():
    assert passed([95, 70, 40]) == 2
    