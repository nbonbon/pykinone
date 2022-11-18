from datetime import datetime
from dateutil import tz

class TimeUtil:
    @staticmethod
    def utcToLocal(utcTime, to_zone):
        from_zone = tz.gettz('UTC')
        utcTime = utcTime.replace(tzinfo=from_zone)
        return utcTime.astimezone(to_zone)

    @staticmethod
    def localToUtc(localTime, from_zone):
        to_zone = tz.gettz('UTC')
        localTime = localTime.replace(tzinfo=from_zone)
        return localTime.astimezone(to_zone)
