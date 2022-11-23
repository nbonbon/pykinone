import sys
import argparse
from dateutil import tz
import dateutil.parser as dateparser
from datetime import datetime
from datetime import timedelta
from zoneinfo import available_timezones
from Entity.TemperatureUnit import TemperatureUnit

class PlotterArgParser:
    def __init__(self):
        self.timezone = "UTC"
        self.temperatureUnits = TemperatureUnit.Celsius
        self.startDate = None
        self.endDate = None
        self.parser = None

    def parseArgs(self, args):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-t", "--temperature",
                            help="temperature units. Default: Celsius, Options: [[c]elsius], [[f]ahrenheit]")
        self.parser.add_argument("-tz", "--timezone",
                            help="timezone to display dates [Default: UTC]")
        self.parser.add_argument("-d", "--daterange",
                            help="Date range to plot data for [Default: last 24 hours]. Format: 'startdate,enddate' with date in ISO 8601 format. NOTE: The use of quotes.")

        parsed_args = self.parser.parse_args(args)

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
            print(argparse.ArgumentTypeError('Timezone was not a valid timezone'))
            self.parser.print_help()
            sys.exit(1)

    @property
    def temperatureUnits(self):
        return self._temperatureUnits
    
    @temperatureUnits.setter
    def temperatureUnits(self, value):
        if value is None:
            self._temperatureUnits = TemperatureUnit.Celsius
        else:
            vLower = value.lower()
            if (vLower == TemperatureUnit.Celsius) or (vLower == TemperatureUnit.Fahrenheit):
                self._temperatureUnits = vLower
            elif vLower == "celsius":
                self._temperatureUnits = TemperatureUnit.Celsius
            elif vLower == "fahrenheit":
                self._temperatureUnits = TemperatureUnit.Fahrenheit
            else:
                self.parser.print_help()
                print(argparse.ArgumentTypeError('Temperature units must be [c(elsius)] or [f(ahrenheit)]'))
                self.parser.print_help()
                sys.exit(1)

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
            startDateTime = endDateTime  - timedelta(days=1)
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