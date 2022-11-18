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
