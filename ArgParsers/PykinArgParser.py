import argparse
import logging

class PykinArgParser:
    def __init__(self):
        self.verbosityLevel = logging.INFO

    def parseArgs(self, args):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-v", "--verbosity", help="Verbosity level. Default: 2, Options: [1-5]", type=int)

        parsed_args = self.parser.parse_args(args)
        self.verbosityLevel = parsed_args.verbosity
    
    @property
    def verbosityLevel(self):
        return self._verbosityLevel
    
    @verbosityLevel.setter
    def verbosityLevel(self, value):
        if value is None:
            self._verbosityLevel = logging.INFO
        else:
            self._verbosityLevel = (value * 10)