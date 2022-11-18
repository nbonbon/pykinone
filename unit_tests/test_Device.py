import json
from Entity.Device import Device

def test_deviceParse():
    testJson = {
        "id": "123",
        "name": "name0",
        "model": "model1",
        "firmwareVersion": "firmwareVersion2"
    }

    device = Device(json.dumps(testJson))
    assert device.id == "123"
    assert device.name == "name0"
    assert device.model == "model1"
    assert device.firmwareVersion == "firmwareVersion2"

def test_eq_are_equal():
    testJson = {
        "id": "123",
        "name": "name0",
        "model": "model1",
        "firmwareVersion": "firmwareVersion2"
    }

    device1 = Device(json.dumps(testJson))
    device2 = Device(json.dumps(testJson))

    assert device1 == device2

def test_eq_are_not_equal():
    testJson1 = {
        "id": "123",
        "name": "name0",
        "model": "model1",
        "firmwareVersion": "firmwareVersion2"
    }

    testJson2 = {
        "id": "123",
        "name": "name01",
        "model": "model1",
        "firmwareVersion": "firmwareVersion2"
    }

    device1 = Device(json.dumps(testJson1))
    device2 = Device(json.dumps(testJson2))

    assert device1 != device2

