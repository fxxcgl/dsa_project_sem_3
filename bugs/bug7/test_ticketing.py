from ticketing import valid_age, valid_score, validate_form, submit

def test_valid_age_normal():
    assert valid_age(30) is True

def test_valid_score_normal():
    assert valid_score(50) is True

def test_validate_edge():
    assert validate_form(30, 100) is True

def test_submit_normal():
    assert submit(30, 50) == "ok"

def test_submit_edge():
    assert submit(30, 0) == "ok"