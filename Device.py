import json

class Device:
    def __init__(self, jsonStr):
        deviceJson = json.loads(jsonStr)
        self.id = deviceJson['id']
        self.name = deviceJson['name']
        self.name = deviceJson['model']
        self.firmwareVersion = deviceJson['firmwareVersion']