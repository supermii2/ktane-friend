MODULE_NAME = "wires"

data = {}

def solve(arr, case_data):
    
    for wire in arr:
        if wire != "red" and wire != "black" and wire != "white" and wire != "yellow" and wire != "blue":
            return "ERROR"

    from tools.baseTools import toOrdinal
    text = "Cut "

    if len(arr) == 3:
        if "red" in arr:
            text += toOrdinal(2)
        elif arr[-1] == "white":
            text += toOrdinal(3)
        elif arr.count("blue") > 1:
            d = max(loc for loc, val in enumerate(arr) if val == 'blue')
            text += toOrdinal(d)
        else:
            text += toOrdinal(3)

    elif len(arr) == 4:
        if arr.count("red") > 1 and int(case_data["serial"][-1]) % 2 == 1:
            text += toOrdinal(max(loc for loc, val in enumerate(arr) if val == 'red'))
        elif arr[-1] == "yellow" and "red" not in arr:
            text += toOrdinal(1)
        elif arr.count("blue") == 1:
            text += toOrdinal(1)
        elif arr.count("yellow") > 1:
            text += toOrdinal(4)
        else:
            text += toOrdinal(2)
    
    elif len(arr) == 5:
        if arr[-1] == "black" and int(case_data["serial"][-1]) % 2 == 1:
            text += toOrdinal(4)
        elif arr.count("red") == 1 and arr.count("yellow") > 1:
            text += toOrdinal(1)
        elif "black" not in arr:
            text += toOrdinal(2)
        else:
            text += toOrdinal(1)

    elif len(arr) == 6:
        if "yellow" not in arr and int(case_data["serial"][-1]) % 2 == 1:
            text += toOrdinal(3)
        elif arr.count("yellow") == 1 and arr.count("white") > 1:
            text += toOrdinal(4)
        elif "red" not in arr:
            text += toOrdinal(6)
        else:
            text += toOrdinal(4)
    else:
        return "ERROR"

    return text

def clear_data():
    pass