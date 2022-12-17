import argparse
import logging
from constants import *

DEFAULT_LOG_FILE = "pykinone.log"
DEFAULT_CONFIG_FILE = "pykinone.conf"

class PykinArgParser:
    def __init__(self):
        self.verbosityLevel = logging.INFO
        self.logFile = DEFAULT_LOG_FILE
        self.configFile = DEFAULT_CONFIG_FILE
        self.databaseFile = DEFAULT_DATABASE_FILE
        self.logfileVerbosity = logging.WARNING

    def parseArgs(self, args):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-v", "--verbosity", help="Verbosity level. Default: 2, Options: [1-5]", type=int)
        self.parser.add_argument("-lv", "--logverbosity", help="Verbosity level for the log file. Default: 3, Options: [1-5]", type=int)
        self.parser.add_argument("-l", "--logfile", help="Log file path. Default: 'pykinone.log'")
        self.parser.add_argument("-c", "--config", help="Config file path. Default: 'pykinone.conf'")
        self.parser.add_argument("-d", "--database", help="Database file path. Default: 'pykinone.db'")

        parsed_args = self.parser.parse_args(args)
        self.verbosityLevel = parsed_args.verbosity
        self.logFile = parsed_args.logfile
        self.configFile = parsed_args.config
        self.databaseFile = parsed_args.database
        self.logfileVerbosity = parsed_args.logverbosity
    
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
    def logfileVerbosity(self):
        return self._logfileVerbosity
    
    @logfileVerbosity.setter
    def logfileVerbosity(self, value):
        if value is None:
            self._logfileVerbosity = logging.WARNING
        else:
            self._logfileVerbosity = (value * 10)

    @property
    def logFile(self):
        return self._logFile
    
    @logFile.setter
    def logFile(self, value):
        if value is None:
            self._logFile = DEFAULT_LOG_FILE
        else:
            self._logFile = value

    @property
    def configFile(self):
        return self._configFile
    
    @configFile.setter
    def configFile(self, value):
        if value is None:
            self._configFile = DEFAULT_CONFIG_FILE
        else:
            self._configFile = value

    @property
    def databaseFile(self):
        return self._databaseFile
    
    @databaseFile.setter
    def databaseFile(self, value):
        if value is None:
            self._databaseFile = DEFAULT_DATABASE_FILE
        else:
            self._databaseFile = value