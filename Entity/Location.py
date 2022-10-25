import json
from Entity.Device import Device

class Location:
    def __init__(self, jsonStr):
        locationJson = json.loads(jsonStr)
        self._name = locationJson['locationName']
        self._devices = []
        devicesJson = locationJson['devices']
        for deviceJson in devicesJson:
            device = Device(json.dumps(deviceJson))
            self.devices.append(device)

    def toString(self):
        result = "Location Name: " + self.name + "\n"
        for device in self.devices:
            result += device.toString()
        return result

    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if self.name != other.name:
            return False
        for i in range(len(self.devices)):
            if self.devices[i] != other.devices[i]:
                return False
        return True

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def devices(self):
        return self._devices
    
    @devices.setter
    def devices(self, value):
        self._devices = value