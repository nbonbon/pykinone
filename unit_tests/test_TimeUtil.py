from datetime import datetime
from dateutil import tz

from Util.TimeUtil import TimeUtil

def test_utcToTimezone_EST():
    utc = datetime.fromisoformat("2022-11-18 20:17:43")
    to_zone = tz.gettz('America/Indiana/Indianapolis') 

    result = TimeUtil.utcToTimezone(utc, to_zone)

    assert result.isoformat(" ","seconds") == "2022-11-18 15:17:43-05:00"

def test_utcToTimezone_UTCtoUTC():
    utc = datetime.fromisoformat("2022-11-18 20:17:43")
    to_zone = tz.gettz('UTC') 

    result = TimeUtil.utcToTimezone(utc, to_zone)

    assert result.isoformat(" ","seconds") == "2022-11-18 20:17:43+00:00"

def test_timezoneToUtc_EST():
    est = datetime.fromisoformat("2022-11-18 15:17:43")
    from_zone = tz.gettz('America/Indiana/Indianapolis') 
    
    result = TimeUtil.timezoneToUtc(est, from_zone)

    assert result.isoformat(" ","seconds") == "2022-11-18 20:17:43+00:00"

def test_timezoneToUtc_UTC():
    utc = datetime.fromisoformat("2022-11-18 15:17:43")
    from_zone = tz.gettz('GMT')
    
    result = TimeUtil.timezoneToUtc(utc, from_zone)

    assert result.isoformat(" ","seconds") == "2022-11-18 15:17:43+00:00"

def test_transformUtcToLocal_datetimes():
    utcs = [
        datetime.fromisoformat("2022-01-01 01:01:01"),
        datetime.fromisoformat("2022-02-02 02:02:02"), 
        datetime.fromisoformat("2022-03-03 03:03:03"),
        datetime.fromisoformat("2022-04-04 04:04:04")
    ]

    result = TimeUtil.transformUtcToTimezone(utcs, tz.gettz('America/Chicago'))

    assert len(utcs) == len(result)
    assert result[0].isoformat(" ","seconds") == "2021-12-31 19:01:01-06:00"
    assert result[1].isoformat(" ","seconds") == "2022-02-01 20:02:02-06:00"
    assert result[2].isoformat(" ","seconds") == "2022-03-02 21:03:03-06:00"
    assert result[3].isoformat(" ","seconds") == "2022-04-03 23:04:04-05:00"

def test_transformUtcToLocal_datetimestrings():
    utcs = [
        "2022-01-01 01:01:01",
        "2022-02-02 02:02:02", 
        "2022-03-03 03:03:03",
        "2022-04-04 04:04:04"
    ]

    result = TimeUtil.transformUtcToTimezone(utcs, tz.gettz('America/Chicago'))

    assert len(utcs) == len(result)
    assert result[0].isoformat(" ","seconds") == "2021-12-31 19:01:01-06:00"
    assert result[1].isoformat(" ","seconds") == "2022-02-01 20:02:02-06:00"
    assert result[2].isoformat(" ","seconds") == "2022-03-02 21:03:03-06:00"
    assert result[3].isoformat(" ","seconds") == "2022-04-03 23:04:04-05:00"

def test_transformLocalToUtc_datetimes():
    locals = [
        datetime.fromisoformat("2022-01-01 01:01:01"),
        datetime.fromisoformat("2022-02-02 02:02:02"), 
        datetime.fromisoformat("2022-03-03 03:03:03"),
        datetime.fromisoformat("2022-04-04 04:04:04")
    ]

    result = TimeUtil.transformTimezoneToUtc(locals, tz.gettz('America/Chicago'))

    assert len(locals) == len(result)
    assert result[0].isoformat(" ","seconds") == "2022-01-01 07:01:01+00:00"
    assert result[1].isoformat(" ","seconds") == "2022-02-02 08:02:02+00:00"
    assert result[2].isoformat(" ","seconds") == "2022-03-03 09:03:03+00:00"
    assert result[3].isoformat(" ","seconds") == "2022-04-04 09:04:04+00:00"

def test_transformLocalToUtc_datetimestrings():
    locals = [
        "2022-01-01 01:01:01",
        "2022-02-02 02:02:02", 
        "2022-03-03 03:03:03",
        "2022-04-04 04:04:04"
    ]

    result = TimeUtil.transformTimezoneToUtc(locals, tz.gettz('America/Chicago'))

    assert len(locals) == len(result)
    assert result[0].isoformat(" ","seconds") == "2022-01-01 07:01:01+00:00"
    assert result[1].isoformat(" ","seconds") == "2022-02-02 08:02:02+00:00"
    assert result[2].isoformat(" ","seconds") == "2022-03-03 09:03:03+00:00"
    assert result[3].isoformat(" ","seconds") == "2022-04-04 09:04:04+00:00"