from datetime import datetime
from dateutil import tz

class TimeUtil:
    @staticmethod
    def utcToTimezone(utcTime, to_zone):
        from_zone = tz.gettz('UTC')
        utcTime = utcTime.replace(tzinfo=from_zone)
        return utcTime.astimezone(to_zone)

    @staticmethod
    def timezoneToUtc(time, from_zone):
        to_zone = tz.gettz('UTC')
        time = time.replace(tzinfo=from_zone)
        return time.astimezone(to_zone)

    @staticmethod
    def transformUtcToTimezone(utcs, to_zone):
        locals = []
        for utc in utcs:
            curTime = utc
            if type(utc) is str:
                curTime = datetime.fromisoformat(utc)
            locals.append(TimeUtil.utcToTimezone(curTime, to_zone))
        return locals

    @staticmethod
    def transformTimezoneToUtc(times, from_zone):
        utcs = []
        for time in times:
            curTime = time
            if type(time) is str:
                curTime = datetime.fromisoformat(time)
            utcs.append(TimeUtil.timezoneToUtc(curTime, from_zone))
        return utcs
