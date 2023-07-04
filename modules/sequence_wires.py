from .tools.natoToLetter import natoToLetter

MODULE_NAME = "sequence"
CLASS_NAME = "ModuleSequenceWires"

class ModuleSequenceWires():
    from enum import Enum

    VALID_COLORS = ["red", "blue", "black"]
    VALID_LETTERS = ["alpha", "bravo", "charlie"]
    CUT_IF_SEQUENCE = [
        ['c', 'b', 'a', 'ac', 'b', 'ac', 'abc', 'ab', 'b'],
        ['b', 'ac', 'b', 'a', 'b', 'bc', 'c', 'ac', 'a'],
        ['abc', 'ac', 'b', 'ac', 'b', 'bc', 'ab', 'c', 'c']
    ]
    def __init__(self, device):
        self.device = device
        self.wire_desc = []
        self.wire_depth = [0, 0, 0]
    
    class Colors(Enum):
        red = 0
        blue = 1
        black = 2

    def compute_wire(self, wire):
        pass

    def handle(self, word):
        if len(self.wire_desc) == 0 and word in ModuleSequenceWires.VALID_COLORS:
            self.wire_desc.append(word)

        elif word in ModuleSequenceWires.VALID_LETTERS:
            cutIf = ModuleSequenceWires.CUT_IF_SEQUENCE
            letter = natoToLetter(word)
            color = self.wire_desc[0]
            depth = self.wire_depth[ModuleSequenceWires.Colors[color]]

            if letter in cutIf[ModuleSequenceWires.Colors[color]][depth]:
                depth += 1
                return "Cut"
            else:
                depth += 1
                return "Next"
        else:
            raise ValueError
