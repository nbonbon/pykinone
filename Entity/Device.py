import json

class Device:
    def __init__(self, jsonStr):
        deviceJson = json.loads(jsonStr)
        self.id = deviceJson['id']
        self.name = deviceJson['name']
        self.model = deviceJson['model']
        self.firmwareVersion = deviceJson['firmwareVersion']

    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if self.id != other.id:
            return False
        if self.name != other.name:
            return False
        if self.model != other.model:
            return False 
        if self.firmwareVersion != other.firmwareVersion:
            return False
        return True

    def toString(self):
        result = "Device Id: " + self.id + "\n"
        result += "Name: " + self.name + "\n"
        result += "Model: " + self.model + "\n"
        result += "Firmware Version: " + self.firmwareVersion + "\n"
        return result