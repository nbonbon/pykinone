import json
from unittest.mock import Mock
from Entity.Location import Location

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

def test_eq_are_equal():
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
    location1 = Location(json.dumps(testJson))
    location2 = Location(json.dumps(testJson))
    assert location1 == location2

def test_eq_are_not_equal():
    testJson1 = {
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
    testJson2 = {
        "locationName": "locationName2",
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
    location1 = Location(json.dumps(testJson1))
    location2 = Location(json.dumps(testJson2))
    assert location1 != location2

def test_shouldNotAddInvalidDevice():
    testJson = {
        "locationName": "locationName1",
        "devices": 
        [
            {
                "id": "id1",
                "RPM": "hundids",
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
    assert location.isValid() == True
    assert len(location.devices) == 1
    assert location.devices[0].name == "name2"

def test_EmptyJson():
    testJson = []

    location = Location(json.dumps(testJson))
    assert location.isValid() == False

def test_NoneJson():
    testJson = None

    location = Location(testJson)
    assert location.isValid() == False

def test_InvalidJson():
    testJson = [
        {
            "nickname": "nicky"
        }
    ]

    location = Location(json.dumps(testJson))
    assert location.isValid() == False