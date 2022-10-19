import os, sys
import json
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from Location import Location

def test_oneDevice():
    testJson = {
        "locationName": "locationName0",
        "devices": 
        [
            {
                "id": "id1",
                "name": "name2",
                "model": "model3",
                "firmwareVersion": "firmwareVersion4"
            }
        ]
    }

    location = Location(json.dumps(testJson))
    assert location.name == "locationName0"
    assert len(location.devices) == 1
    assert location.devices[0].id == "id1"

def test_multipleDevices():
    testJson = {
        "locationName": "locationName1",
        "devices": 
        [
            {
                "id": "id1",
                "name": "name1",
                "model": "model1",
                "firmwareVersion": "firmwareVersion1"
            },
            {
                "id": "id2",
                "name": "name2",
                "model": "model2",
                "firmwareVersion": "firmwareVersion2"
            },
        ]
    }

    location = Location(json.dumps(testJson))
    assert location.name == "locationName1"
    assert len(location.devices) == 2
    assert location.devices[0].id == "id1"
    assert location.devices[1].id == "id2"