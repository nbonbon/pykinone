import argparse
from dateutil import tz
from zoneinfo import available_timezones

class TimezoneAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values in available_timezones():
            timezone = tz.gettz(values)
            setattr(namespace, self.dest, timezone)
        else:
            print('got here')
            argparse.ArgumentTypeError('Timezone was not a valid timezone')