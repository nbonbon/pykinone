import sys
import json
import argparse
from random import *
from datetime import datetime
from datetime import timedelta
from DbUtil.DbManager import DbManager
from Entity.Location import Location
from Entity.ThermostatInfo import ThermostatInfo

def run():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--two",
                        help="Database with 2 days of data always unique every 3 minutes (start: 2022-02-02 00:00:00, end: 2022-02-03 23:59:59)", action='store_true')
    group.add_argument("-o", "--onehundred",
                        help="Database with 100 rows. Using current time.", action='store_true')

    parsed_args = parser.parse_args(sys.argv[1:])

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

    if parsed_args.onehundred:
        print("Creating db with 100 entries...")
        currentDateTime = datetime.now()
        for i in range(100):
            info = ThermostatInfo(json.dumps(testThemostatInfoJson), "testId")
            info.time = currentDateTime.isoformat(" ","seconds")
            info.tempOutdoor = i
            dbManager.save(info)
            currentDateTime = currentDateTime + timedelta(minutes=3)
    elif parsed_args.two:
        print("Creating db with 2 days worth of entries...")
        currentDateTime = datetime.fromisoformat("2022-02-02 00:00:00")
        lastValue = None
        for day in range(2):
            for hour in range(24):
                for minute in range(0, 60, 3):
                    info = ThermostatInfo(json.dumps(testThemostatInfoJson), "testId")
                    info.tempOutdoor = hour
                    newTemp = randint(0, 30) # just to ensure something has changed
                    if newTemp == lastValue:
                        newTemp = newTemp + 1
                    lastValue = newTemp
                    info.tempIndoor = newTemp
                    info.time = currentDateTime.isoformat(" ","seconds")
                    dbManager.save(info)
                    currentDateTime = currentDateTime + timedelta(minutes=3)

    dbManager.close()

run()