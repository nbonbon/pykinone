import argparse
import logging

DEFAULT_LOG_FILE = "pykinone.log"

class PykinArgParser:
    def __init__(self):
        self.verbosityLevel = logging.INFO
        self.logFile = DEFAULT_LOG_FILE

    def parseArgs(self, args):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-v", "--verbosity", help="Verbosity level. Default: 2, Options: [1-5]", type=int)
        self.parser.add_argument("-l", "--logfile", help="Log file path. Default: 'pykinone.log'")

        parsed_args = self.parser.parse_args(args)
        self.verbosityLevel = parsed_args.verbosity
        self.logFile = parsed_args.logfile
    
    @property
    def verbosityLevel(self):
        return self._verbosityLevel
    
    @verbosityLevel.setter
    def verbosityLevel(self, value):
        if value is None:
            self._verbosityLevel = logging.INFO
        else:
            self._verbosityLevel = (value * 10)

    @property
    def logFile(self):
        return self._logFile
    
    @logFile.setter
    def logFile(self, value):
        if value is None:
            self._logFile = DEFAULT_LOG_FILE
        else:
            self._logFile = value