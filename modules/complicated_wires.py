MODULE_NAME = "complex"
CLASS_NAME = "ModuleComplicatedWires"

class ModuleComplicatedWires():
    from enum import Enum
    VALID_WORDS = ["red", "blue", "star", "light"]

    COMPLICATED_WIRES_TABLE = [
        [
            [['C', 'C'], ['D', 'B']],
            [['S', 'D'], ['P', 'P']]
        ],
        [
            [['S', 'B'], ['C', 'B']],
            [['S', 'S'], ['P', 'D']]
        ]
    ]

    class WireDesc(Enum):
        red = 0
        blue = 1
        star = 2
        light = 3

    def __init__(self, device):
        self.device = device
        self.wire_memory = []
        self.description_memory = [False, False, False, False]
    
    

    def compute_wire(self, wire):
        table = ModuleComplicatedWires.COMPLICATED_WIRES_TABLE       
        instruction = table[wire[0]][wire[1]][wire[2]][wire[3]]

        if instruction == 'C':
            return 'Cut'
        elif instruction == 'D':
            return 'Skip'
        elif instruction == 'P':
            return 'Cut' if "parallel" in self.device.get_data("ports") else "Skip"
        elif instruction == 'S':
            return 'Cut' if self.device.get_data("batteries") >= 2 else "Skip"
        else:
            return "Cut" if int(self.device.get_data("identifier")[-1])


    def handle(self, word):
        if word == "space":
            self.wire_memory.append(self.description_memory)
            self.description_memory = [False, False, False, False]
        
        elif word in ModuleComplicatedWires.VALID_WORDS:
            self.description_memory[ModuleComplicatedWires.WireDesc[word]] = True

        elif word == "finish":
            text = ""
            for wire in self.wire_memory:
                text += self.compute_wire() + " "

            return text
        
                
