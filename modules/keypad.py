
#See Readme for button identification
#TODO: add readme
from module import Module
class ModuleKeypad(Module):
    VALID_KEYPADS = set("quebec", 
                        "alpha", 
                        "lambda", 
                        "bolt", 
                        "cat", 
                        "hotel", 
                        "back", 
                        "echo", 
                        "swirl", 
                        "white", 
                        "question", 
                        "copyright",
                        "nose",
                        "xray",
                        "three",
                        "paragraph",
                        "six",
                        "bravo",
                        "smile",
                        "trident",
                        "front",
                        "snake",
                        "black",
                        "equals",
                        "ash",
                        "omega",
                        "november")
    
    VALID_SEQUENCES = set(
        ["quebec", "alpha", "lambda", "bolt", "cat", "hotel", "back"],
        ["echo", "quebec", "back", "swirl", "white", "hotel", "question"],
        ["copyright", "nose", "swirl", "xray", "three", "lambda", "white"],
        ["six", "paragraph", "bravo", "cat", "xray", "question", "smile"],
        ["trident", "smile", "bravo", "front", "paragraph", "snake", "black"],
        ["six", "echo", "equals", "ash", "trident", "november", "omega"]
    )

    def __init__(self, device):
        super(device)
        self.progress = set()


    def process_keypads(self):
        for seq in ModuleKeypad.VALID_SEQUENCES:
            if all(map(lambda keypad: keypad in seq, self.progress)):
                return ModuleKeypad.find_sequence_order(seq)
        #TODO: Handle Error

    def find_sequence_order(self, seq):
        correct_order = sorted(map(lambda item: (seq.index(item), item), self.progress))
        response = ""
        for keypad in correct_order:
            response += keypad[1] + " "
        return response 



    def handle(self, word):
        if word in ModuleKeypad.VALID_KEYPADS:
            self.progress.add(word)
        else:
            #TODO: ERROR HANDLING
            pass

        if len(self.progress) == 4:
            ModuleKeypad.process_keypads()
        