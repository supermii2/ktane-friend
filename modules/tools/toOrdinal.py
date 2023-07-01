ORDINAL_NAMES = {
    0 : "th",
    1 : "st",
    2 : "nd",
    3 : "rd",
    4 : "th",
    5 : "th",
    6 : "th",
    7 : "th",
    8 : "th",
    9 : "th",
}

def toOrdinal(num: int) -> str:
    return str(num) + ORDINAL_NAMES[num % 10]