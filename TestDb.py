import time
import json
from DbUtil.DbManager import DbManager
from Entity.Location import Location
from Entity.ThermostatInfo import ThermostatInfo

def run():
    dbManager = DbManager()
    
    # create location / device
    testLocationJson = {
        "locationName": "testLocation",
        "devices": 
        [
            {
                "id": "testId",
                "name": "testName",
                "model": "testModel",
                "firmwareVersion": "testFirmwareVersion"
            }
        ]
    }
    location = Location(json.dumps(testLocationJson))
    dbManager.save(location)

    testThemostatInfoJson = {
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
        "tempIndoor": 20.5,
        "humIndoor": 50,
        "tempOutdoor": 0,
        "humOutdoor": 50.1,
        "scheduleEnabled": False,
        "geofencingEnabled": False
    }

    # Fill 100 rows
    # for i in range(100):
    #     info = ThermostatInfo(json.dumps(testThemostatInfoJson), "testId")
    #     print("Before: " + str(info.tempOutdoor))
    #     info.tempOutdoor = i
    #     print("After: " + str(info.tempOutdoor))
    #     dbManager.save(info)
    #     print("Saving therminfo: " + str(i))
    #     time.sleep(1)

    # create themostat_infos
        # Create data for 2 days. Every hour has temp set to hour number
            # need to be able to set the time or else this will take forever to create
    dbManager.close()

run()