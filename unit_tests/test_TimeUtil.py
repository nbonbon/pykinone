from datetime import datetime
from dateutil import tz

from Util.TimeUtil import TimeUtil

def test_utcToLocal_EST():
    utc = datetime.fromisoformat("2022-11-18 20:17:43")
    to_zone = tz.gettz('America/Indiana/Indianapolis') 

    result = TimeUtil.utcToLocal(utc, to_zone)

    assert result.isoformat(" ","seconds") == "2022-11-18 15:17:43-05:00"

def test_utcToLocal_UTCtoUTC():
    utc = datetime.fromisoformat("2022-11-18 20:17:43")
    to_zone = tz.gettz('UTC') 

    result = TimeUtil.utcToLocal(utc, to_zone)

    assert result.isoformat(" ","seconds") == "2022-11-18 20:17:43+00:00"

def test_localToUtc_EST():
    est = datetime.fromisoformat("2022-11-18 15:17:43")
    from_zone = tz.gettz('America/Indiana/Indianapolis') 
    
    result = TimeUtil.localToUtc(est, from_zone)

    assert result.isoformat(" ","seconds") == "2022-11-18 20:17:43+00:00"

def test_localToUtc_UTC():
    utc = datetime.fromisoformat("2022-11-18 15:17:43")
    from_zone = tz.gettz('GMT') 
    
    result = TimeUtil.localToUtc(utc, from_zone)

    assert result.isoformat(" ","seconds") == "2022-11-18 15:17:43+00:00"

def test_transformUtcToLocal():
    utcs = [
        datetime.fromisoformat("2022-01-01 01:01:01"),
        datetime.fromisoformat("2022-02-02 02:02:02"), 
        datetime.fromisoformat("2022-03-03 03:03:03"),
        datetime.fromisoformat("2022-04-04 04:04:04")
    ]

    result = TimeUtil.transformUtcToLocal(utcs, tz.gettz('America/Chicago'))

    assert len(utcs) == len(result)
    assert result[0].isoformat(" ","seconds") == "2021-12-31 19:01:01-06:00"
    assert result[1].isoformat(" ","seconds") == "2022-02-01 20:02:02-06:00"
    assert result[2].isoformat(" ","seconds") == "2022-03-02 21:03:03-06:00"
    assert result[3].isoformat(" ","seconds") == "2022-04-03 23:04:04-05:00"

def test_transformLocalToUtc():
    locals = [
        datetime.fromisoformat("2022-01-01 01:01:01"),
        datetime.fromisoformat("2022-02-02 02:02:02"), 
        datetime.fromisoformat("2022-03-03 03:03:03"),
        datetime.fromisoformat("2022-04-04 04:04:04")
    ]

    result = TimeUtil.transformLocalToUtc(locals, tz.gettz('America/Chicago'))

    assert len(locals) == len(result)
    assert result[0].isoformat(" ","seconds") == "2022-01-01 07:01:01+00:00"
    assert result[1].isoformat(" ","seconds") == "2022-02-02 08:02:02+00:00"
    assert result[2].isoformat(" ","seconds") == "2022-03-03 09:03:03+00:00"
    assert result[3].isoformat(" ","seconds") == "2022-04-04 09:04:04+00:00"