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