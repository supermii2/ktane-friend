from .tools.morseToLetter import morseToLetter

MODULE_NAME = "morse"
CLASS_NAME = "ModuleMorse"

class ModuleMorse():
    VALID_MORSE = {"dot": ".", "dash" : "-"}

    VALID_WORDS = {
        "shell" : "3.505",
        "halls" : "3.515",
        "slick" : "3.522",
        "trick" : "3.532",
        "boxes" : "3.535",
        "leaks" : "3.542",
        "strobe" : "3.545",
        "bistro" : "3.552",
        "flick" : "3.555",
        "bombs" : "3.565",
        "break" : "3.572",
        "brick" : "3.575",
        "steak" : " 3.582",
        "sting" : "3.592",
        "vector" : "3.595",
        "beats" : "3.600"
    }

    def __init__(self, device):
        self.device = device
        self.word_memory = ""
        self.morse_memory = ""
    
    def handle(self, word):
        if word in ModuleMorse.VALID_MORSE:
            self.morse_memory += ModuleMorse.VALID_MORSE[word]

        elif word == "space":
            self.word_memory += morseToLetter(self.morse_memory)
            self.morse_memory = ""

            if self.word_memory in ModuleMorse.VALID_WORDS:
                return ModuleMorse.VALID_WORDS[self.word_memory]
        
        else:
            raise ValueError
        
                
