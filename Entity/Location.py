import json
from Entity.Device import Device

class Location:
    def __init__(self, jsonStr):
        if jsonStr is not None:
            locationJson = json.loads(jsonStr)
            if 'locationName' in locationJson:
                self.name = locationJson['locationName']
            self.devices = []
            if 'devices' in locationJson:
                devicesJson = locationJson['devices']
                for deviceJson in devicesJson:
                    device = Device(json.dumps(deviceJson))
                    if device.isValid():
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

    def isValid(self):
        return ((hasattr(self, "name") and (getattr(self, "name") is not None)) and
                (hasattr(self, "devices") and (getattr(self, "devices") is not None)))

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def devices(self):
        return self._devices
    
    @devices.setter
    def devices(self, value):
        self._devices = value