from .tools.toOrdinal import toOrdinal

MODULE_NAME = "wires"
CLASS_NAME = "ModuleWires"

class ModuleWires():
    def __init__(self, device):
        self.device = device
        self.data = []

    def process_wires(self):
        text = "Cut "
        if len(self.data) == 3:
            if "red" in self.data:
                text += toOrdinal(2)
            elif self.data[-1] == "white":
                text += toOrdinal(3)
            elif self.data.count("blue") > 1:
                d = max(loc for loc, val in enumerate(self.data) if val == 'blue')
                text += toOrdinal(d)
            else:
                text += toOrdinal(3)
        elif len(self.data) == 4:
            if self.data.count("red") > 1 and int(self.device.get_data('serial')[-1]) % 2 == 1:
                text += toOrdinal(max(loc for loc, val in enumerate(self.data) if val == 'red'))
            elif self.data[-1] == "yellow" and "red" not in self.data:
                text += toOrdinal(1)
            elif self.data.count("blue") == 1:
                text += toOrdinal(1)
            elif self.data.count("yellow") > 1:
                text += toOrdinal(4)
            else:
                 text += toOrdinal(2)
        elif len(self.data) == 5:
            if self.data[-1] == "black" and int(self.device.get_data('serial')[-1]) % 2 == 1:
                text += toOrdinal(4)
            elif self.data.count("red") == 1 and self.data.count("yellow") > 1:
                text += toOrdinal(1)
            elif "black" not in self.data:
                text += toOrdinal(2)
            else:
                text += toOrdinal(1)
        elif len(self.data) == 6:
            if "yellow" not in self.data and int(self.device.get_data('serial')[-1]) % 2 == 1:
                text += toOrdinal(3)
            elif self.data.count("yellow") == 1 and self.data.count("white") > 1:
                text += toOrdinal(4)
            elif "red" not in self.data:
                text += toOrdinal(6)
            else:
                text += toOrdinal(4)
        else:
            return "ERROR"  
        
        return text
    def handle(self, word):
        if word == 'space':
            return self.process_wires()
        else:
            self.data.append(word)