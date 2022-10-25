import json

class ThermostatInfo:
    def __init__(self, jsonStr=None, deviceId=None):
        if jsonStr != None:
            thermostatInfoJson = json.loads(jsonStr)
            self.equipmentStatus = thermostatInfoJson['equipmentStatus']
            self.mode = thermostatInfoJson['mode']
            self.modeLimit = thermostatInfoJson['modeLimit']
            self.modeEmHeatAvailable = thermostatInfoJson['modeEmHeatAvailable']
            self.fan = thermostatInfoJson['fan']
            self.fanCirculate = thermostatInfoJson['fanCirculate']
            self.fanCirculateSpeed = thermostatInfoJson['fanCirculateSpeed']
            self.heatSetpoint = thermostatInfoJson['heatSetpoint']
            self.coolSetpoint = thermostatInfoJson['coolSetpoint']
            self.setpointDelta = thermostatInfoJson['setpointDelta']
            self.setpointMinimum = thermostatInfoJson['setpointMinimum']
            self.setpointMaximum = thermostatInfoJson['setpointMaximum']
            self.tempIndoor = thermostatInfoJson['tempIndoor']
            self.humIndoor = thermostatInfoJson['humIndoor']
            self.tempOutdoor = thermostatInfoJson['tempOutdoor']
            self.humOutdoor = thermostatInfoJson['humOutdoor']
            self.scheduleEnabled = thermostatInfoJson['scheduleEnabled']
            self.geofencingEnabled = thermostatInfoJson['geofencingEnabled']
            self.deviceId = deviceId

    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if self.equipmentStatus != other.equipmentStatus:
            return False
        if self.mode != other.mode:
            return False
        if self.modeLimit != other.modeLimit:
            return False 
        if self.modeEmHeatAvailable != other.modeEmHeatAvailable:
            return False
        if self.fan != other.fan:
            return False
        if self.fanCirculate != other.fanCirculate:
            return False
        if self.fanCirculateSpeed != other.fanCirculateSpeed:
            return False
        if self.heatSetpoint != other.heatSetpoint:
            return False
        if self.coolSetpoint != other.coolSetpoint:
            return False
        if self.setpointDelta != other.setpointDelta:
            return False
        if self.setpointMinimum != other.setpointMinimum:
            return False
        if self.setpointMaximum != other.setpointMaximum:
            return False
        if self.tempIndoor != other.tempIndoor:
            return False
        if self.humIndoor != other.humIndoor:
            return False
        if self.tempOutdoor != other.tempOutdoor:
            return False
        if self.humOutdoor != other.humOutdoor:
            return False
        if self.scheduleEnabled != other.scheduleEnabled:
            return False
        if self.geofencingEnabled != other.geofencingEnabled:
            return False
        if self.deviceId != other.deviceId:
            return False
        return True

    def toString(self):
        result = "Equipment Status: " + str(self.equipmentStatus) + "\n"
        result += "Mode: " + str(self.mode) + "\n"
        result += "Mode Limit: " + str(self.modeLimit) + "\n"
        result += "Mode Emergency Heat Available: " + str(self.modeEmHeatAvailable) + "\n"
        result += "Fan: " + str(self.fan) + "\n"
        result += "Fan Circulate: " + str(self.fanCirculate) + "\n"
        result += "Fan Circulate Speed: " + str(self.fanCirculateSpeed) + "\n"
        result += "Heat Set Point: " + str(self.heatSetpoint) + "\n"
        result += "Cool Set Point: " + str(self.coolSetpoint) + "\n"
        result += "Set Point Delta: " + str(self.setpointDelta) + "\n"
        result += "Set Point Minimum: " + str(self.setpointMinimum) + "\n"
        result += "Set Point Maximum: " + str(self.setpointMaximum) + "\n"
        result += "Temperature Indoor: " + str(self.tempIndoor) + "\n"
        result += "Humidity Indoor: " + str(self.humIndoor) + "\n"
        result += "Temperature Outdoor: " + str(self.tempOutdoor) + "\n"
        result += "Humidity Outdoor: " + str(self.humOutdoor) + "\n"
        result += "Schedule Enabled: " + str(self.scheduleEnabled) + "\n"
        result += "Geofencing Enabled: " + str(self.geofencingEnabled) + "\n"
        return result
    
    @property
    def equipmentStatus(self):
        return self._equipmentStatus
    
    @equipmentStatus.setter
    def equipmentStatus(self, value):
        self._equipmentStatus = int(value)

    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, value):
        self._mode = int(value)
    
    @property
    def modeLimit(self):
        return self._modeLimit
    
    @modeLimit.setter
    def modeLimit(self, value):
        self._modeLimit = int(value)

    @property
    def modeEmHeatAvailable(self):
        return self._modeEmHeatAvailable
    
    @modeEmHeatAvailable.setter
    def modeEmHeatAvailable(self, value):
        self._modeEmHeatAvailable = int(value)
    
    @property
    def fan(self):
        return self._fan
    
    @fan.setter
    def fan(self, value):
        self._fan = int(value)

    @property
    def fanCirculate(self):
        return self._fanCirculate
    
    @fanCirculate.setter
    def fanCirculate(self, value):
        self._fanCirculate = int(value)

    @property
    def fanCirculateSpeed(self):
        return self._fanCirculateSpeed
    
    @fanCirculateSpeed.setter
    def fanCirculateSpeed(self, value):
        self._fanCirculateSpeed = int(value)

    @property
    def heatSetpoint(self):
        return self._heatSetpoint
    
    @heatSetpoint.setter
    def heatSetpoint(self, value):
        self._heatSetpoint = float(value)

    @property
    def coolSetpoint(self):
        return self._coolSetpoint
    
    @coolSetpoint.setter
    def coolSetpoint(self, value):
        self._coolSetpoint = float(value)

    @property
    def setpointDelta(self):
        return self._setpointDelta
    
    @setpointDelta.setter
    def setpointDelta(self, value):
        self._setpointDelta = float(value)

    @property
    def setpointMinimum(self):
        return self._setpointMinimum
    
    @setpointMinimum.setter
    def setpointMinimum(self, value):
        self._setpointMinimum = float(value)

    @property
    def setpointMaximum(self):
        return self._setpointMaximum
    
    @setpointMaximum.setter
    def setpointMaximum(self, value):
        self._setpointMaximum = float(value)

    @property
    def tempIndoor(self):
        return self._tempIndoor
    
    @tempIndoor.setter
    def tempIndoor(self, value):
        self._tempIndoor = float(value)

    @property
    def humIndoor(self):
        return self._humIndoor
    
    @humIndoor.setter
    def humIndoor(self, value):
        self._humIndoor = float(value)

    @property
    def tempOutdoor(self):
        return self._tempOutdoor
    
    @tempOutdoor.setter
    def tempOutdoor(self, value):
        self._tempOutdoor = float(value)

    @property
    def humOutdoor(self):
        return self._humOutdoor
    
    @humOutdoor.setter
    def humOutdoor(self, value):
        self._humOutdoor = float(value)

    @property
    def scheduleEnabled(self):
        return self._scheduleEnabled
    
    @scheduleEnabled.setter
    def scheduleEnabled(self, value):
        self._scheduleEnabled = bool(value)

    @property
    def geofencingEnabled(self):
        return self._geofencingEnabled
    
    @geofencingEnabled.setter
    def geofencingEnabled(self, value):
        self._geofencingEnabled = bool(value)

    @property
    def deviceId(self):
        return self._deviceId
    
    @deviceId.setter
    def deviceId(self, value):
        self._deviceId = str(value)