MODULE_NAME = "sequence"
CLASS_NAME = "ModuleSequenceWires"

class ModuleSequenceWires():
    from enum import Enum

    VALID_COLORS = ["red", "blue", "black"]
    VALID_LETTERS = ["alpha", "bravo", "charlie"]

    def __init__(self, device):
        self.device = device
        self.wire_desc = []
        self.wire_depth = []
    
    def Colors(Enum):
        red = 0
        blue = 1
        black = 2

    def compute_wire(self, wire):
        pass

    def handle(self, word):
        if len(self.wire_desc) == 0 and word in ModuleSequenceWires.VALID_COLORS:
            