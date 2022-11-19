import argparse

class PlotterArgParser:
    @staticmethod
    def parseArgs(args):
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--temp",
                            help="temperature units. Default: Celsius, Options: [[C]elsius], [[F]ahrenheit]", default="C")
        parser.add_argument("-tz", "--timezone",
                            help="timezone to display dates [Default: local timezone]", default="utc")
        parser.add_argument("-d", "--daterange",
                            help="Date range to plot data for [Default: last 24 hours]. Format: (startdate:enddate) with date in yyyy-mm-dd format.")
        return parser.parse_args(args)