from typing import Optional

class InputHandler:
    
    POSSIBLE_MODULES = []
    
    def __init__(self):
        self.mode = 'default'
        self.module_data = InputHandler.init_modules()
        self.working_modules = {}
        self.device_data = {}

    def process_input(self, words: list[str]) -> Optional(list[str]):
        for word in words:
            InputHandler.handle_input_word(word)

    
    def handle_input_word(self, word: str) -> Optional(str):
        if self.mode == 'default':
            #TODO: Add Failsafe
            self.mode = word
            self.working_modules[word] = InputHandler.module_data[word].__init__()

        elif word == 'exit':
            self.working_modules.remove(self.mode)
            self.mode = 'default'

        else:
            self.working_modules[self.mode].handle_word(self, word)

    def get_data(self, keyword):
        return self.data[keyword]

    def init_modules(self) -> dict:
        pass