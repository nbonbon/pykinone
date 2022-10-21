import time
import config
import requests
from DbUtil.DbManager import DbManager

DAIKIN_ONE_BASE_URI = "https://integrator-api.daikinskyport.com"
AUTH_TOKEN_ENDPOINT_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/token"
DEVICES_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/devices"
SECONDS_IN_ONE_MINUTE = 60
MINIMUM_QUERY_SPAN = 3 * 60

integratorToken = ""
integratorEmail = ""
apiKey = ""

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
            authTimeout = time.time() + int(authResponseJson['accessTokenExpiresIn'])
        
        if not intialized:
            deviceResponseJson = getDevices(authResponseJson)
            intialized = True
        
        getDeviceInfo(authResponseJson, deviceResponseJson)
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
        print("Configuration file loaded...")
    else:
        print("Error loading config file")
    return

def initializeRestApiWithIntegratorToken():
    print("Initializing integration token with REST API...")
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
    print("Getting devices...")
    headers = {
        'x-api-key': apiKey,
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + authResponseJson['accessToken']
    }
    devicesResponse = requests.get(DEVICES_URI_PATH, headers=headers)
    return devicesResponse.json()

def getDeviceInfo(authResponseJson, deviceResponseJson):
    print("Getting device info...")
    deviceId = deviceResponseJson[0]['devices'][0]['id']
    headers = {
        'x-api-key': apiKey,
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + authResponseJson['accessToken']
    }
    deviceInfoResponse = requests.get(DEVICES_URI_PATH + '/' + deviceId, headers=headers)
    print(deviceInfoResponse.json())

run()