class InputHandler:
    
    POSSIBLE_MODULES = ['device_init', 'wires', 'buttons']
    
    def __init__(self):
        self.mode = 'default'
        #A Dictionary Containing KVPS of Module Name to Module Class
        self.module_data = self.init_modules()
        self.working_modules = {}
        self.device_data = {}

    def process_input(self, words):
        for word in words:
            self.handle_input_word(word)

    
    def handle_input_word(self, word):
        try:
            if self.mode == 'default':
                if word not in self.module_data:
                    raise ValueError("Invalid Module Name")
                
                self.mode = word
                self.working_modules[word] = self.module_data[word](self)

            elif word == 'exit':
                self.working_modules.remove(self.mode)
                self.mode = 'default'

            else:
                output_str = self.working_modules[self.mode].handle(word)
                if output_str != None:
                    print(output_str)

        except ValueError:
            #TODO:
            print("Error")
            pass

    def get_data(self, keyword):
        return self.device_data[keyword]

    def init_modules(self) -> dict:
        module_names = map(lambda x: "modules." + x, InputHandler.POSSIBLE_MODULES)
        all_modules_required = list(map(__import__, module_names))[0]
        modules_available = map(lambda x: getattr(all_modules_required, x), InputHandler.POSSIBLE_MODULES)
        module_dict = dict(list(map(lambda x: (getattr(x, "MODULE_NAME"), getattr(x, getattr(x, "CLASS_NAME"))), modules_available)))
        return module_dict
        

a = InputHandler()
a.process_input(['initialize', 'ports', 'rj45'])

