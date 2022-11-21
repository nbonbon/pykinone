import argparse
from dateutil import tz
import dateutil.parser as dateparser
from datetime import datetime
from datetime import timedelta
from zoneinfo import available_timezones

class PlotterArgParser:
    def __init__(self):
        self.timezone = "UTC"
        self.temperatureUnits = "c"
        self.startDate = None
        self.endDate = None

    def parseArgs(self, args):
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--temperature",
                            help="temperature units. Default: Celsius, Options: [[c]elsius], [[f]ahrenheit]")
        parser.add_argument("-tz", "--timezone",
                            help="timezone to display dates [Default: UTC]")
        parser.add_argument("-d", "--daterange",
                            help="Date range to plot data for [Default: last 24 hours]. Format: 'startdate,enddate' with date in ISO 8601 format.")

        parsed_args = parser.parse_args(args)

        self.timezone = parsed_args.timezone
        self.temperatureUnits = parsed_args.temperature
        self.daterange = self._parseDates(parsed_args.daterange)

    @property
    def timezone(self):
        return self._timezone
    
    @timezone.setter
    def timezone(self, value):
        if value is None:
            self._timezone = tz.gettz("UTC")
        elif type(value) is str and value in available_timezones():
            self._timezone = tz.gettz(value)
        elif type(value) is tz.tzfile:
            self._timezone = value
        else:
            argparse.ArgumentTypeError('Timezone was not a valid timezone')

    @property
    def temperatureUnits(self):
        return self._temperatureUnits
    
    @temperatureUnits.setter
    def temperatureUnits(self, value):
        if value is None:
            self._temperatureUnits = "c"
        else:
            vLower = value.lower()
            if (vLower == "c") or (vLower == "f"):
                self._temperatureUnits = vLower
            elif vLower == "celsius":
                self._temperatureUnits = "c"
            elif vLower == "fahrenheit":
                self._temperatureUnits = "f"
            else:
                argparse.ArgumentTypeError('Temperature units must be [c(elsius)] or [f(ahrenheit)]')

    @property
    def startDate(self):
        return self._startDate
    
    @startDate.setter
    def startDate(self, value):
        self._startDate = value

    @property
    def endDate(self):
        return self._endDate
    
    @endDate.setter
    def endDate(self, value):
        self._endDate = value

    def _parseDates(self, dateRangeStr):
        if dateRangeStr is None:
            endDateTime = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            print("Today: " + endDateTime.isoformat())
            startDateTime = endDateTime  - timedelta(days=1)
            print("Yesterday: " + startDateTime.isoformat())
            self.endDate = endDateTime
            self.startDate = startDateTime
        else:
            splitDates = dateRangeStr.split(",")
            if len(splitDates) != 2:
                argparse.ArgumentTypeError("Daterange must comply to format: 'startdate,enddate' with date in ISO 8601 format.")
            startDateTime = datetime.fromisoformat(splitDates[0])
            self.startDate = startDateTime
            endDateTime = datetime.fromisoformat(splitDates[1])
            self.endDate = endDateTime