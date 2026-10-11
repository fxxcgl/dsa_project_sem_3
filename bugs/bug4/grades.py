def letter(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score > 70:
        return "C"
    return "F"

def report(scores):
    out = []
    for s in scores:
        out.append(letter(s))
    return ",".join(out)

def passed(scores):
    count = 0
    for s in scores:
        if letter(s) != "F":
            count += 1
    return count
