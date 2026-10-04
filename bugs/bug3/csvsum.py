def parse(s):
    return s.split(",")

def to_ints(parts):
    return list(map(int, parts))

def total(s):
    return sum(to_ints(parse(s))) + 1