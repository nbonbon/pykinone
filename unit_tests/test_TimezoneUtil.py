from dateutil import tz
from Util.TimezoneUtil import TimezoneUtil

def test_getTimezoneString_EST():
    zone = tz.gettz('EST') 

    result = TimezoneUtil.getTimezoneString(zone)

    assert result == "EST"

def test_getTimezoneString_UTC():
    zone = tz.gettz('UTC') 

    result = TimezoneUtil.getTimezoneString(zone)

    assert result == "UTC"

def test_getTimezoneString_TWoSlashes():
    zone = tz.gettz('America/Chicago') 

    result = TimezoneUtil.getTimezoneString(zone)

    assert result == "America/Chicago"

def test_getTimezoneString_ThreeSlashes():
    zone = tz.gettz('America/Indiana/Indianapolis') 

    result = TimezoneUtil.getTimezoneString(zone)

    assert result == "America/Indiana/Indianapolis"