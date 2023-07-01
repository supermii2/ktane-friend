MODULE_NAME = "simon"
CLASS_NAME = "ModuleSimon"

class ModuleSimon():
    from enum import Enum
    SIMON_TABLE = [
        [
            ['Blue', 'Red', 'Yellow', 'Green'],
            ['Yellow', 'Green', 'Blue', 'Red'],
            ['Green', 'Red', 'Yellow', 'Blue']
        ],
        [
            ['Blue', 'Yellow', 'Green', 'Red'],
            ['Red', 'Blue', 'Yellow', 'Green'],
            ['Yellow', 'Green', 'Blue', 'Red']
        ]
    ]

    class Colors(Enum):
        RED = 0
        BLUE = 1
        GREEN = 2
        YELLOW = 3
    
    def __init__(self, device):
        self.device = device
    
    def hasNoVowel(input):
        return 0 if 'a' in input or 'e' in input or 'i' in input or 'o' in input or 'u' in input else 1

    def handle(self, word):
        return ModuleSimon.SIMON_TABLE[self.hasNoVowel(self.device.get_data('serial'))]\
            [self.device.get_data('strikes')][ModuleSimon.Colors[word].value]