from csvsum import parse, to_ints, total

def test_parse():
    assert parse("1,2") == ["1", "2"]

def test_total():
    assert total("1,2,3") == 6