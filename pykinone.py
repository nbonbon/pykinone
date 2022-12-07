import sys
import time
import config
import json
import requests
import logging
from DbUtil.DbManager import DbManager
from DevicesResponseUtil import DevicesResponseUtil
from Entity.ThermostatInfo import ThermostatInfo
from ArgParsers.PykinArgParser import PykinArgParser

DAIKIN_ONE_BASE_URI = "https://integrator-api.daikinskyport.com"
AUTH_TOKEN_ENDPOINT_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/token"
DEVICES_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/devices"
SECONDS_IN_ONE_MINUTE = 60
MINIMUM_QUERY_SPAN = 3 * 60

parser = PykinArgParser()
parser.parseArgs(sys.argv[1:])
verbosityLevel = parser.verbosityLevel

integratorToken = ""
integratorEmail = ""
apiKey = ""

logger = logging.getLogger(__name__)
logger.setLevel(verbosityLevel)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def run():
    authTimeout = 0
    loadConfiguration()
    dbManager = DbManager()
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
                dbManager.save(thermInfo)
                logger.info(thermInfo.toString())
        time.sleep(MINIMUM_QUERY_SPAN)

    dbManager.close()

def loadConfiguration():
    cfg = config.Config("pykinone.conf")
    if cfg:
        global integratorToken
        integratorToken = cfg['integratorToken']
        global integratorEmail
        integratorEmail = cfg['integratorEmail']
        global apiKey
        apiKey = cfg['apiKey']
        logger.debug("Configuration file loaded...")
    else:
        logger.error("Error loading config file")
    return

def initializeRestApiWithIntegratorToken():
    logger.debug("Initializing integration token with REST API...")
    headers = {
        'x-api-key': apiKey,
        'Content-Type': 'application/json'
    }
    data = {
        'email': integratorEmail, 
        'integratorToken': integratorToken
    }
    authResponse = requests.post(AUTH_TOKEN_ENDPOINT_URI_PATH, json=data, headers=headers)
    return authResponse.json()

def getDevices(authResponseJson):
    logger.debug("Getting devices...")
    headers = {
        'x-api-key': apiKey,
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + authResponseJson['accessToken']
    }
    devicesResponse = requests.get(DEVICES_URI_PATH, headers=headers)
    return devicesResponse.json()

def getThermostatInfo(authResponseJson, deviceId):
    logger.debug("Getting device info...")
    headers = {
        'x-api-key': apiKey,
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + authResponseJson['accessToken']
    }
    deviceInfoResponse = requests.get(DEVICES_URI_PATH + '/' + deviceId, headers=headers)
    return deviceInfoResponse.json()

run()