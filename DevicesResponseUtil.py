import json
from Entity.Location import Location

class DevicesResponseUtil:

    @staticmethod
    def parseDevicesResponse(jsonStr):
        locationList = []

        if jsonStr is None:
            return locationList

        locationsJson = json.loads(jsonStr)
        
        for locationJson in locationsJson:
            location = Location(json.dumps(locationJson))
            if location.isValid():
                locationList.append(location)

        return locationList