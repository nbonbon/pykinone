import json

class ThermostatInfo:
    def __init__(self, jsonStr):
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
        result += "Humidty Indoor: " + str(self.humIndoor) + "\n"
        result += "Temperature Indoor: " + str(self.tempOutdoor) + "\n"
        result += "Humidity Outdoor: " + str(self.humOutdoor) + "\n"
        result += "Schedule Enabled: " + str(self.scheduleEnabled) + "\n"
        result += "Geofencing Enabled: " + str(self.geofencingEnabled) + "\n"
        return result