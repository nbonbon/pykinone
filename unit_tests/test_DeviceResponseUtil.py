import json
from DevicesResponseUtil import DevicesResponseUtil

def test_oneLocation():
    testJson = [
        {
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
    ]

    locations = DevicesResponseUtil.parseDevicesResponse(json.dumps(testJson))
    assert len(locations) == 1
    assert locations[0].name == "locationName0"
    assert len(locations[0].devices) == 1
    assert locations[0].devices[0].name == "name2"

def test_multipleLocations():
    testJson = [
        {
            "locationName": "locationName1",
            "devices": 
            [
                {
                    "id": "id1",
                    "name": "name1",
                    "model": "model1",
                    "firmwareVersion": "firmwareVersion1"
                }
            ]
        },
        {
            "locationName": "locationName2",
            "devices": 
            [
                {
                    "id": "id2",
                    "name": "name2",
                    "model": "model2",
                    "firmwareVersion": "firmwareVersion2"
                },
                {
                    "id": "id3",
                    "name": "name3",
                    "model": "model3",
                    "firmwareVersion": "firmwareVersion3"
                }
            ]
        }
    ]

    locations = DevicesResponseUtil.parseDevicesResponse(json.dumps(testJson))
    assert len(locations) == 2
    assert locations[1].name == "locationName2"
    assert len(locations[1].devices) == 2
    assert locations[1].devices[1].model == "model3"