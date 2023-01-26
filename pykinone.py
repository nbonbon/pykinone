import sys
import time
import config
import json
import requests
import logging
import threading
from DbUtil.DbManager import DbManager
from DevicesResponseUtil import DevicesResponseUtil
from Entity.ThermostatInfo import ThermostatInfo
from ArgParsers.PykinArgParser import PykinArgParser
from ble.SwitchbotMeterScanner import SwitchbotMeterScanner

DAIKIN_ONE_BASE_URI = "https://integrator-api.daikinskyport.com"
AUTH_TOKEN_ENDPOINT_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/token"
DEVICES_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/devices"
SECONDS_IN_ONE_MINUTE = 60
MINIMUM_QUERY_SPAN = 3 * 60

parser = PykinArgParser()
parser.parseArgs(sys.argv[1:])
verbosityLevel = parser.verbosityLevel
logFile = parser.logFile
configFile = parser.configFile
databaseFile = parser.databaseFile
logfileVerbosity = parser.logfileVerbosity

integratorToken = ""
integratorEmail = ""
apiKey = ""

logger = logging.getLogger('MainLogger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
streamHandler.setLevel(verbosityLevel)

fileHandler = logging.FileHandler(logFile)
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logfileVerbosity)

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

def run():
    logger.info("Starting...")
    authTimeout = 0
    loadConfiguration()
    dbManager = DbManager(databaseFile)
    sbScanner = SwitchbotMeterScanner()
    temperatureMonitorThread = threading.Thread(target=sbScanner.scanForSwitchbotMeters)
    temperatureMonitorThread.start()
    running = True
    intialized = False
    while running:
        now = time.time()
        if now > authTimeout:
            authResponseJson = initializeRestApiWithIntegratorToken()
            authTimeout = time.time() + int(authResponseJson['accessTokenExpiresIn']) - 1 # subtract one to give a buffer
        
        if not intialized:
            deviceResponseJson = getDevices(authResponseJson)
            locations = DevicesResponseUtil.parseDevicesResponse(json.dumps(deviceResponseJson))
            for location in locations:
                dbManager.save(location)
            intialized = True
        
        for location in locations:
            for device in location.devices:
                thermostatInfoJson = getThermostatInfo(authResponseJson, device.id)
                thermInfo = ThermostatInfo(json.dumps(thermostatInfoJson), device.id)
                if thermInfo.isValid():
                    dbManager.save(thermInfo)
                    logger.debug("\n" + thermInfo.toString())
                else:
                    logger.debug("Invalid thermostat info object.")
        
        meters = sbScanner.getMeters()
        for meter in meters.values():
            logger.debug('\n' + meter.toString())
        time.sleep(MINIMUM_QUERY_SPAN)

    logger.info("Shutting down...")
    temperatureMonitorThread.join()
    dbManager.close()

def loadConfiguration():
    cfg = config.Config(configFile)
    if cfg:
        global integratorToken
        integratorToken = cfg['integratorToken']
        global integratorEmail
        integratorEmail = cfg['integratorEmail']
        global apiKey
        apiKey = cfg['apiKey']
        logger.info("Configuration file loaded...")
    else:
        logger.error("Error loading config file")
    return

def initializeRestApiWithIntegratorToken():
    logger.info("Initializing integration token with REST API...")
    headers = {
        'x-api-key': apiKey,
        'Content-Type': 'application/json'
    }
    data = {
        'email': integratorEmail, 
        'integratorToken': integratorToken
    }
    
    try:
        authResponse = requests.post(AUTH_TOKEN_ENDPOINT_URI_PATH, json=data, headers=headers)
        return authResponse.json()
    except requests.exceptions.RequestException as e:
        logger.exception("Error: Could not authenticate with API.\n" + e)

def getDevices(authResponseJson):
    logger.info("Getting devices...")
    headers = {
        'x-api-key': apiKey,
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + authResponseJson['accessToken']
    }

    try:
        devicesResponse = requests.get(DEVICES_URI_PATH, headers=headers)
        return devicesResponse.json()
    except requests.exceptions.RequestException as e:
        logger.exception("Error: Could not retrieve devices.\n" + e)

def getThermostatInfo(authResponseJson, deviceId):
    logger.info("Getting device info...")
    headers = {
        'x-api-key': apiKey,
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + authResponseJson['accessToken']
    }

    try:
        deviceInfoResponse = requests.get(DEVICES_URI_PATH + '/' + deviceId, headers=headers)
        return deviceInfoResponse.json()
    except requests.exceptions.RequestException as e:
        logger.exception("Error: Could not retrieve thermostat info.\n" + e)

run()