# Collection of useful functions for use in other modules

NATO_ALPHABET = {
    "alfa" : "a",
    "beta" : "b",
    "charlie" : "c",
    "delta" : "d",
    "echo" : "e",
    "foxtrot" : "f",
    "golf" : "g",
    "hotel" : "h",
    "india" : "i",
    "juliett" : "j",
    "kilo" : "k",
    "lima" : "l",
    "mike" : "m",
    "november" : "n",
    "oscar" : "o",
    "papa" : "p",
    "quebec" : "q",
    "romeo" : "r",
    "sierra" : "s",
    "tango" : "t",
    "uniform" : "u",
    "victor" : "v",
    "whiskey" : "w",
    "xray" : "x",
    "yankee" : "y",
    "zulu" : "z",

    "alpha" : "a",
    "juliet" : "j",

    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "0" : "0",
}

def natoToLetter(natoWord: str) -> str:
    return NATO_ALPHABET[natoWord]

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