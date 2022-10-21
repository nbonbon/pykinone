import json

class Device:
    def __init__(self, jsonStr):
        deviceJson = json.loads(jsonStr)
        self.id = deviceJson['id']
        self.name = deviceJson['name']
        self.model = deviceJson['model']
        self.firmwareVersion = deviceJson['firmwareVersion']

    def toString(self):
        result = "Device Id: " + self.id + "\n"
        result += "Name: " + self.name + "\n"
        result += "Model: " + self.model + "\n"
        result += "Firmware Version: " + self.firmwareVersion + "\n"
        return result