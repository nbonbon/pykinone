import logging
from ArgParsers.PykinArgParser import PykinArgParser

def test_parseArgs_defaults():
    args = []

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.verbosityLevel == logging.INFO
    assert parser.logFile == "pykinone.log"

def test_parseArgs_verbosity_shortOption():
    args = ['-v', '5']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.verbosityLevel == logging.CRITICAL

def test_parseArgs_logFileverbosity():
    args = ['-lv', '5']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.logfileVerbosity == logging.CRITICAL

def test_verbosity_longOption():
    args = ['--verbosity', '4']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.verbosityLevel == logging.ERROR

def test_parseArgs_logFile_shortOption():
    args = ['-l', '/etc/logfile.log']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.logFile == "/etc/logfile.log"

def test_parseArgs_logFile_longOption():
    args = ['--logfile', '/etc/logfile.log']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.logFile == "/etc/logfile.log"

def test_parseArgs_configFile_shortOption():
    args = ['-c', '/etc/config.conf']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.configFile == "/etc/config.conf"

def test_parseArgs_configFile_longOption():
    args = ['--config', '/etc/config.conf']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.configFile == "/etc/config.conf"

def test_parseArgs_databaseFile_shortOption():
    args = ['-d', 'db.db']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.databaseFile == "db.db"

def test_parseArgs_databaseFile_longOption():
    args = ['--database', 'db.db']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.databaseFile == "db.db"