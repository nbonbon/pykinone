class TimezoneUtil:
    @staticmethod
    def getTimezoneString(timezone):
        timezoneStr = str(timezone)
        startIndex = timezoneStr.index("zoneinfo/") + len("zoneinfo/")
        stopIndex = timezoneStr.index('\')')
        return timezoneStr[startIndex:stopIndex]
