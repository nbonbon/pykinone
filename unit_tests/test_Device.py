import os, sys
import json
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from Device import Device

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

