from module import Module
from tools.natoToLetter import natoToLetter

class DeviceInit(Module):
    VALID_PORTS = ['dvi-d', 'parallel', 'ps2', 'rj45', 'serial', 'rca']
    VALID_BATTERIES = ['aa', 'd']
    VALID_MODES = ['ports', 'batteries', 'indicators', 'serial']
    name = 'init'
    SERIAL_LENGTH = 6
    
    def __init__(self, device_data):
        super(device_data)
        self.current_mode = 'default'
        self.indicator_progress = ""
        self.serial_progress = ""

        for mode in DeviceInit.VALID_MODES:
            device_data[mode] = []
    
    def handle_ports(self, word):
        if word in DeviceInit.VALID_PORTS:
            self.device_data['ports'].append(word)

    def handle_indicators(self, word):
        if word == 'space':
            self.device_data['indicators'].append(self.indicator_progress)
            self.indicator_progress = ""
        else:
            self.indicator_progress += natoToLetter(word)

    def handle_batteries(self, word):
        self.device_data['batteries'].append(word)
    
    def handle_serial(self, word):
        self.serial_progress += natoToLetter(word)
        if len(self.serial_progress) == DeviceInit.SERIAL_LENGTH:
            self.device_data['serial'].append(self.serial_progress)

    def handle(self, word, device):
        if word in DeviceInit.VALID_MODES:
            self.current_mode = word

        elif self.current_mode == 'ports':
            DeviceInit.handle_ports(word)

        elif self.current_mode == "indicators":
            DeviceInit.handle_indicators(word)

        elif self.current_mode == 'batteries':
            DeviceInit.handle_batteries(word)

        elif self.current_mode == 'serial':
            DeviceInit.handle_serial(word)
    




