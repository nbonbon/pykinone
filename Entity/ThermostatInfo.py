import json

class ThermostatInfo:
    def __init__(self, jsonStr=None, deviceId=None):
        self.time = None
        self.deviceId = deviceId
        
        if jsonStr is not None:
            thermostatInfoJson = json.loads(jsonStr)
            if 'equipmentStatus' in thermostatInfoJson:
                self.equipmentStatus = thermostatInfoJson['equipmentStatus']
            if 'mode' in thermostatInfoJson:
                self.mode = thermostatInfoJson['mode']
            if 'modeLimit' in thermostatInfoJson:
                self.modeLimit = thermostatInfoJson['modeLimit']
            if 'modeEmHeatAvailable' in thermostatInfoJson:
                self.modeEmHeatAvailable = thermostatInfoJson['modeEmHeatAvailable']
            if 'fan' in thermostatInfoJson:
                self.fan = thermostatInfoJson['fan']
            if 'fanCirculate' in thermostatInfoJson:
                self.fanCirculate = thermostatInfoJson['fanCirculate']
            if 'fanCirculateSpeed' in thermostatInfoJson:
                self.fanCirculateSpeed = thermostatInfoJson['fanCirculateSpeed']
            if 'heatSetpoint' in thermostatInfoJson:
                self.heatSetpoint = thermostatInfoJson['heatSetpoint']
            if 'coolSetpoint' in thermostatInfoJson:
                self.coolSetpoint = thermostatInfoJson['coolSetpoint']
            if 'setpointDelta' in thermostatInfoJson:
                self.setpointDelta = thermostatInfoJson['setpointDelta']
            if 'setpointMinimum' in thermostatInfoJson:
                self.setpointMinimum = thermostatInfoJson['setpointMinimum']
            if 'setpointMaximum' in thermostatInfoJson:
                self.setpointMaximum = thermostatInfoJson['setpointMaximum']
            if 'tempIndoor' in thermostatInfoJson:
                self.tempIndoor = thermostatInfoJson['tempIndoor']
            if 'humIndoor' in thermostatInfoJson:
                self.humIndoor = thermostatInfoJson['humIndoor']
            if 'tempOutdoor' in thermostatInfoJson:
                self.tempOutdoor = thermostatInfoJson['tempOutdoor']
            if 'humOutdoor' in thermostatInfoJson:
                self.humOutdoor = thermostatInfoJson['humOutdoor']
            if 'scheduleEnabled' in thermostatInfoJson:
                self.scheduleEnabled = thermostatInfoJson['scheduleEnabled']
            if 'geofencingEnabled' in thermostatInfoJson:
                self.geofencingEnabled = thermostatInfoJson['geofencingEnabled']

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
        result = "\tEquipment Status: " + str(self.equipmentStatus) + "\n"
        result += "\tMode: " + str(self.mode) + "\n"
        result += "\tMode Limit: " + str(self.modeLimit) + "\n"
        result += "\tMode Emergency Heat Available: " + str(self.modeEmHeatAvailable) + "\n"
        result += "\tFan: " + str(self.fan) + "\n"
        result += "\tFan Circulate: " + str(self.fanCirculate) + "\n"
        result += "\tFan Circulate Speed: " + str(self.fanCirculateSpeed) + "\n"
        result += "\tHeat Set Point: " + str(self.heatSetpoint) + "\n"
        result += "\tCool Set Point: " + str(self.coolSetpoint) + "\n"
        result += "\tSet Point Delta: " + str(self.setpointDelta) + "\n"
        result += "\tSet Point Minimum: " + str(self.setpointMinimum) + "\n"
        result += "\tSet Point Maximum: " + str(self.setpointMaximum) + "\n"
        result += "\tTemperature Indoor: " + str(self.tempIndoor) + "\n"
        result += "\tHumidity Indoor: " + str(self.humIndoor) + "\n"
        result += "\tTemperature Outdoor: " + str(self.tempOutdoor) + "\n"
        result += "\tHumidity Outdoor: " + str(self.humOutdoor) + "\n"
        result += "\tSchedule Enabled: " + str(self.scheduleEnabled) + "\n"
        result += "\tGeofencing Enabled: " + str(self.geofencingEnabled) + "\n"
        return result

    def isValid(self):
        return ((hasattr(self, "equipmentStatus") and (getattr(self, "equipmentStatus") is not None)) and
        (hasattr(self, "mode") and (getattr(self, "mode") is not None))and
        (hasattr(self, "modeLimit") and (getattr(self, "modeLimit") is not None))and
        (hasattr(self, "modeEmHeatAvailable") and (getattr(self, "modeEmHeatAvailable") is not None))and
        (hasattr(self, "fan") and (getattr(self, "fan") is not None))and
        (hasattr(self, "fanCirculate") and (getattr(self, "fanCirculate") is not None))and
        (hasattr(self, "fanCirculateSpeed") and (getattr(self, "fanCirculateSpeed") is not None))and
        (hasattr(self, "heatSetpoint") and (getattr(self, "heatSetpoint") is not None))and
        (hasattr(self, "coolSetpoint") and (getattr(self, "coolSetpoint") is not None))and
        (hasattr(self, "setpointDelta") and (getattr(self, "setpointDelta") is not None))and
        (hasattr(self, "setpointMinimum") and (getattr(self, "setpointMinimum") is not None))and
        (hasattr(self, "setpointMaximum") and (getattr(self, "setpointMaximum") is not None))and
        (hasattr(self, "tempIndoor") and (getattr(self, "tempIndoor") is not None))and
        (hasattr(self, "humIndoor") and (getattr(self, "humIndoor") is not None))and
        (hasattr(self, "tempOutdoor") and (getattr(self, "tempOutdoor") is not None))and
        (hasattr(self, "humOutdoor") and (getattr(self, "humOutdoor") is not None))and
        (hasattr(self, "scheduleEnabled") and (getattr(self, "scheduleEnabled") is not None))and
        (hasattr(self, "geofencingEnabled") and (getattr(self, "geofencingEnabled") is not None)))
    
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, value):
        self._time = value

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