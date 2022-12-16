import json

class Device:
    def __init__(self, jsonStr):
        if jsonStr is not None:
            deviceJson = json.loads(jsonStr)
            if 'id' in deviceJson:
                self.id = deviceJson['id']
            if 'name' in deviceJson:
                self.name = deviceJson['name']
            if 'model' in deviceJson:
                self.model = deviceJson['model']
            if 'firmwareVersion' in deviceJson:
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

    def isValid(self):
        return ((hasattr(self, "id") and (getattr(self, "id") is not None)) and
        (hasattr(self, "name") and (getattr(self, "name") is not None))and
        (hasattr(self, "model") and (getattr(self, "model") is not None))and
        (hasattr(self, "firmwareVersion") and (getattr(self, "firmwareVersion") is not None)))

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = str(value)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = str(value)

    @property
    def firmwareVersion(self):
        return self._firmwareVersion
    
    @firmwareVersion.setter
    def firmwareVersion(self, value):
        self._firmwareVersion = str(value)