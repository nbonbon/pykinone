import json
from Entity.Device import Device

class Location:
    def __init__(self, jsonStr):
        locationJson = json.loads(jsonStr)
        self.name = locationJson['locationName']
        self.devices = []
        devicesJson = locationJson['devices']
        for deviceJson in devicesJson:
            device = Device(json.dumps(deviceJson))
            self.devices.append(device)

    def toString(self):
        result = "Location Name: " + self.name + "\n"
        for device in self.devices:
            result += device.toString()
        return result