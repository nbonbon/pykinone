import json
from Entity.ThermostatInfo import ThermostatInfo

def test_thermostatInfoParsing():
    testJson = {
        "equipmentStatus": 1,
        "mode": 2,
        "modeLimit": 3,
        "modeEmHeatAvailable": 0,
        "fan": 1,
        "fanCirculate": 2,
        "fanCirculateSpeed": 1,
        "heatSetpoint": 20.5,
        "coolSetpoint": 23.5,
        "setpointDelta": 2.5,
        "setpointMinimum": 10.0,
        "setpointMaximum": 32.3,
        "tempIndoor": 21.5,
        "humIndoor": 50,
        "tempOutdoor": 20.5,
        "humOutdoor": 50.1,
        "scheduleEnabled": False,
        "geofencingEnabled": False
    }

    info = ThermostatInfo(json.dumps(testJson), "0")
    assert info.equipmentStatus == 1
    assert info.mode == 2
    assert info.modeLimit == 3
    assert info.modeEmHeatAvailable == 0
    assert info.fan == 1
    assert info.fanCirculate == 2
    assert info.fanCirculateSpeed == 1
    assert info.heatSetpoint == 20.5
    assert info.coolSetpoint == 23.5
    assert info.setpointDelta == 2.5
    assert info.setpointMinimum == 10.0
    assert info.setpointMaximum == 32.3
    assert info.tempIndoor == 21.5
    assert info.humIndoor == 50
    assert info.tempOutdoor == 20.5
    assert info.humOutdoor == 50.1
    assert info.scheduleEnabled == False
    assert info.geofencingEnabled == False

def test_eq_are_equal():
    testJson = {
        "equipmentStatus": 1,
        "mode": 2,
        "modeLimit": 3,
        "modeEmHeatAvailable": 0,
        "fan": 1,
        "fanCirculate": 2,
        "fanCirculateSpeed": 1,
        "heatSetpoint": 20.5,
        "coolSetpoint": 23.5,
        "setpointDelta": 2.5,
        "setpointMinimum": 10.0,
        "setpointMaximum": 32.3,
        "tempIndoor": 21.5,
        "humIndoor": 50,
        "tempOutdoor": 20.5,
        "humOutdoor": 50.1,
        "scheduleEnabled": False,
        "geofencingEnabled": False
    }

    info1 = ThermostatInfo(json.dumps(testJson), "0")
    info2 = ThermostatInfo(json.dumps(testJson), "0")
    assert info1 == info2

def test_eq_are_not_equal():
    testJson1 = {
        "equipmentStatus": 1,
        "mode": 2,
        "modeLimit": 3,
        "modeEmHeatAvailable": 0,
        "fan": 1,
        "fanCirculate": 2,
        "fanCirculateSpeed": 1,
        "heatSetpoint": 20.5,
        "coolSetpoint": 23.5,
        "setpointDelta": 2.5,
        "setpointMinimum": 10.0,
        "setpointMaximum": 32.3,
        "tempIndoor": 21.5,
        "humIndoor": 50,
        "tempOutdoor": 20.5,
        "humOutdoor": 50.1,
        "scheduleEnabled": False,
        "geofencingEnabled": False
    }

    testJson2 = {
        "equipmentStatus": 1,
        "mode": 2,
        "modeLimit": 3,
        "modeEmHeatAvailable": 0,
        "fan": 1,
        "fanCirculate": 2,
        "fanCirculateSpeed": 1,
        "heatSetpoint": 20.5,
        "coolSetpoint": 23.5,
        "setpointDelta": 2.5,
        "setpointMinimum": 10.0,
        "setpointMaximum": 32.3,
        "tempIndoor": 21.5,
        "humIndoor": 50,
        "tempOutdoor": 20.5,
        "humOutdoor": 50.2,
        "scheduleEnabled": False,
        "geofencingEnabled": False
    }

    info1 = ThermostatInfo(json.dumps(testJson1), "0")
    info2 = ThermostatInfo(json.dumps(testJson2), "0")
    assert info1 != info2