import json

class Location:
    def __init__(self, jsonStr):
        locationJson = json.loads(jsonStr)
        self.name = locationJson['locationName']