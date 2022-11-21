from datetime import datetime
from datetime import timedelta
from dateutil import tz
from ArgParsers.PlotterArgParser import PlotterArgParser

def test_parseArgs_defaults():
    args = []

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.temperatureUnits == "c"
    assert parser.timezone == tz.gettz("UTC")
    assert parser.startDate.isoformat() == (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  - timedelta(days=1)).isoformat()
    assert parser.endDate.isoformat() ==  datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).isoformat()

def test_parseArgs_tempF_shortOption():
    args = ['-t', 'F']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.temperatureUnits == "f"

def test_parseArgs_tempF_longOption():
    args = ['--temperature', 'F']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.temperatureUnits == "f"

def test_parseArgs_tempF_longValue_Celsius():
    args = ['--temperature', 'Celsius']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.temperatureUnits == "c"

def test_parseArgs_tempF_longValue_Celsius():
    args = ['--temperature', 'Fahrenheit']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.temperatureUnits == "f"

def test_parseArgs_timezone_short():
    args = ['-tz', 'America/Chicago']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.timezone == tz.gettz("America/Chicago")

def test_parseArgs_timezone_long():
    args = ['--timezone', 'America/Cancun']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.timezone == tz.gettz("America/Cancun")


def test_parseArgs_daterange_short():
    args = ['-d', '2022-10-25,2022-10-26']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.startDate.isoformat(' ') == "2022-10-25 00:00:00"
    assert parser.endDate.isoformat(' ') ==  "2022-10-26 00:00:00"

def test_parseArgs_daterange_long():
    args = ['--daterange', '2022-10-25,2022-10-26']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.startDate.isoformat(' ') == "2022-10-25 00:00:00"
    assert parser.endDate.isoformat(' ') ==  "2022-10-26 00:00:00"

def test_parseArgs_daterange_withTimes():
    args = ['--daterange', '2022-10-25 01:01:01,2022-10-26 02:02:02']

    parser = PlotterArgParser()
    parser.parseArgs(args)

    assert parser.startDate.isoformat(' ') == "2022-10-25 01:01:01"
    assert parser.endDate.isoformat(' ') ==  "2022-10-26 02:02:02"