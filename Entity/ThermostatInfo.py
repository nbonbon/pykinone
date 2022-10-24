import json

class ThermostatInfo:
    def __init__(self, jsonStr="", deviceId=-1):
        if jsonStr != "":
            thermostatInfoJson = json.loads(jsonStr)
            self.equipmentStatus = int(thermostatInfoJson['equipmentStatus'])
            self.mode = int(thermostatInfoJson['mode'])
            self.modeLimit = int(thermostatInfoJson['modeLimit'])
            self.modeEmHeatAvailable = int(thermostatInfoJson['modeEmHeatAvailable'])
            self.fan = int(thermostatInfoJson['fan'])
            self.fanCirculate = int(thermostatInfoJson['fanCirculate'])
            self.fanCirculateSpeed = int(thermostatInfoJson['fanCirculateSpeed'])
            self.heatSetpoint = float(thermostatInfoJson['heatSetpoint'])
            self.coolSetpoint = float(thermostatInfoJson['coolSetpoint'])
            self.setpointDelta = float(thermostatInfoJson['setpointDelta'])
            self.setpointMinimum = float(thermostatInfoJson['setpointMinimum'])
            self.setpointMaximum = float(thermostatInfoJson['setpointMaximum'])
            self.tempIndoor = float(thermostatInfoJson['tempIndoor'])
            self.humIndoor = float(thermostatInfoJson['humIndoor'])
            self.tempOutdoor = float(thermostatInfoJson['tempOutdoor'])
            self.humOutdoor = float(thermostatInfoJson['humOutdoor'])
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