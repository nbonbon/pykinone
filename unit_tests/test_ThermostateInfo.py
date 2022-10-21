import os, sys
import json
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
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

    info = ThermostatInfo(json.dumps(testJson))
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