from ArgParsers.PlotterArgParser import PlotterArgParser

def test_parseArgs_defaults():
    args = []

    result = PlotterArgParser.parseArgs(args)

    assert result.temp == "C"
    assert result.timezone == "utc"
    assert result.daterange == None

def test_parseArgs_tempF_short():
    args = ['-t', 'F']

    result = PlotterArgParser.parseArgs(args)

    assert result.temp == "F"

def test_parseArgs_tempF_long():
    args = ['--temp', 'F']

    result = PlotterArgParser.parseArgs(args)

    assert result.temp == "F"

def test_parseArgs_timezone_short():
    args = ['-tz', 'America/Chicago']

    result = PlotterArgParser.parseArgs(args)

    assert result.timezone == "America/Chicago"

def test_parseArgs_timezone_long():
    args = ['--timezone', '	America/Cancun']

    result = PlotterArgParser.parseArgs(args)

    assert result.timezone == "	America/Cancun"

def test_parseArgs_daterange_short():
    args = ['-d', '2022-10-25:2022-10-26']

    result = PlotterArgParser.parseArgs(args)

    assert result.daterange == "2022-10-25:2022-10-26"

def test_parseArgs_daterange_long():
    args = ['--daterange', '2022-10-25:2022-10-26']

    result = PlotterArgParser.parseArgs(args)

    assert result.daterange == "2022-10-25:2022-10-26"