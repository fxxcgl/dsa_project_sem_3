from textutil import clean, shout, first_word, title

def test_clean():
    assert clean("  hi ") == "hi"

def test_shout():
    assert shout(" hi ") == "HI"

def test_first_word():
    assert first_word("hello world") == "hello"

def test_title():
    assert title("hello world") == "Hello"