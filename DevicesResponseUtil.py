import json


import json
from Location import Location

class DevicesResponseUtil:

    @staticmethod
    def parseDevicesResponse(jsonStr):
        locationsJson = json.loads(jsonStr)
        locationList = []
        
        for locationJson in locationsJson:
            location = Location(json.dumps(locationJson))
            locationList.append(location)

        return locationList