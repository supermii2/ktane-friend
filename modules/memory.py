from .tools.toOrdinal import toOrdinal

MODULE_NAME = "memory"
CLASS_NAME = "ModuleMemory"

class ModuleMemory():
    VALID_NUMBERS = ["1", "2", "3", "4"]
    def __init__(self, device):
        self.device = device
        self.stage = 1
        self.stage_memory = []
        self.options = []
    
    def handle(self, word):
        if word not in ModuleMemory.VALID_NUMBERS:
            raise ValueError
        if self.stage == 1:
            self.current_memory.append(word)
            if len(self.options == len(ModuleMemory.VALID_NUMBERS) + 1):
                display = self.options[0]
                if display == "1":
                    self.stage_memory.append(("2", self.options[2]))
                    return "Press " + self.options[2]
                
                
