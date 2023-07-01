from .tools.natoToLetter import natoToLetter

MODULE_NAME = "initialize"
CLASS_NAME = "DeviceInit"

class DeviceInit():
    VALID_PORTS = ['dvi-d', 'parallel', 'ps2', 'rj45', 'serial', 'rca']
    VALID_BATTERIES = ['aa', 'd']
    VALID_MODES = ['ports', 'batteries', 'indicators', 'identifier']
    name = 'init'
    SERIAL_LENGTH = 6
    
    def __init__(self, device):
        self.device_data = device.device_data
        self.current_mode = 'default'
        self.indicator_progress = ""
        self.serial_progress = ""
        self.device_data['strikes'] = 0
        
        for mode in DeviceInit.VALID_MODES:
            self.device_data[mode] = []

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
        self.device_data['batteries'].append(int(word))
    
    def handle_serial(self, word):
        self.serial_progress += natoToLetter(word)
        if len(self.serial_progress) == DeviceInit.SERIAL_LENGTH:
            self.device_data['identifier'].append(self.serial_progress)

    def handle(self, word):
        if word in DeviceInit.VALID_MODES:
            self.current_mode = word

        elif self.current_mode == 'ports':
            self.handle_ports(word)

        elif self.current_mode == "indicators":
            self.handle_indicators(word)

        elif self.current_mode == 'batteries':
            self.handle_batteries(word)

        elif self.current_mode == 'identifier':
            self.handle_serial(word)
        else:
            raise ValueError()


