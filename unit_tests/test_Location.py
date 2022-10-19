import os, sys
import json
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from Location import Location

def test_oneLocation():
    testJson = [
        {
            "locationName": "locationName",
                "devices": [
                {
                    "id": "id",
                    "name": "name",
                    "model": "model",
                    "firmwareVersion": "firmwareVersion"
                }
            ]
        }
    ]

    location = Location(json.dumps(testJson))
    assert location.locationName == "locationName"