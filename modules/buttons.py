MODULE_NAME = "buttons"
CLASS_NAME = "ModuleButton"

class ModuleButton():
    VALID_WORDS = {"abort", "detonate", "hold", "press"}
    VALID_COLORS = {"blue", "red", "white", "yellow"}

    def __init__(self, device):
        self.device = device
        self.word = None
        self.color = None
        self.mode = 'button'

    def process_button(self):
        #TODO: Add error handling
        if self.color == "blue" and self.word == "abort":
            return "Hold Button"
        elif self.device.get_data('batteries') >= 2 and self.word == "detonate":
            return "Press Button"
        elif self.color == "white" and 'car' in self.device.get_data('indicators'):
            return "Hold Button"
        elif self.device.get_data('batteries') >= 3 and 'frk' in self.device.get_data('indicators'):
            return "Press Button"
        elif self.color == "red" and self.word == "hold":
            return "Press Button"
        else:
            return "Hold Button"

    def process_strip(word):
        if word == 'yellow':
            return "Release on five in any position"
        elif word == 'blue':
            return "Release on four in any position"
        else:
            return "Release on one in any position"

    def handle(self, word):
        if self.mode == 'strip':
            ModuleButton.process_strip(word)
            self.mode = 'button'
        else:
            if word in ModuleButton.VALID_WORDS:
                self.word = word
            if word in ModuleButton.VALID_COLORS:
                self.color = word
            if self.word != None and self.color != None:
                ModuleButton.process_button()
                self.mode = "strip"

ModuleButton('h')