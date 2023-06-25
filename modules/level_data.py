data = {}

VALID_EXTENSIONS = ["dvi-d", "parallel", "ps2", "rj45", "serial", "rca"]

def update_data(arr):
    print(arr)
    from tools.baseTools import natoToLetter

    global data
    if arr[0] == "extensions":
        data["extensions"] = list(filter(lambda x: x in VALID_EXTENSIONS, arr[1:]))
        return "Extensions Updated"

    if arr[0] == "batteries":
        try:
            data["batteries"] = int(arr[1])
            return "Batteries Updated"
        except:
            return "Battery Update Failed"
    
    if arr[0] == "identity":
        try:
            data["serial"] = ''.join(list(map(natoToLetter, arr[1:])))
            return "Serial Number Updated"
        except:
            return "Serial Update Failed"

    #TODO: HANDLE INDICATORS



def clear_data():
    data.clear()
    
