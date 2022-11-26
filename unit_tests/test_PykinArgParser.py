import logging
from ArgParsers.PykinArgParser import PykinArgParser

def test_parseArgs_defaults():
    args = []

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.verbosityLevel == logging.INFO

def test_parseArgs_verbosity_shortOption():
    args = ['-v', '5']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.verbosityLevel == logging.CRITICAL

def test_verbosity_tempF_longOption():
    args = ['--verbosity', '4']

    parser = PykinArgParser()
    parser.parseArgs(args)

    assert parser.verbosityLevel == logging.ERROR