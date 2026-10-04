def clean(s):
    return s.strip()

def shout(s):
    return clean(s).upper()

def first_word(s):
    return clean(s).split(" ")[1]

def title(s):
    return first_word(s).capitalize()