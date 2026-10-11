def in_range(value, low, high):
    return low < value < high

def valid_age(age):
    return in_range(age, 0, 120)

def valid_score(score):
    return in_range(score, 0, 100)

def validate_form(age, score):
    return valid_age(age) and valid_score(score)

def submit(age, score):
    if validate_form(age, score):
        return "ok"
    return "rejected"