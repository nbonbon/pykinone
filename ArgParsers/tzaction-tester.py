import sys
import argparse
from TimezoneAction import TimezoneAction
from dateutil import tz

parser = argparse.ArgumentParser()
parser.add_argument("-tz", "--timezone",
                            help="timezone to display dates [Default: UTC]", action=TimezoneAction, default=tz.gettz("UTC"))
args = parser.parse_args(sys.argv[1:])

print(type(args.timezone))
print(args.timezone)