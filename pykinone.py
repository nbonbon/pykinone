import time
import config
import requests

DAIKIN_ONE_BASE_URI = "https://integrator-api.daikinskyport.com"
AUTH_TOKEN_ENDPOINT_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/token"
DEVICES_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/devices"
SECONDS_IN_ONE_MINUTE = 60
MINIMUM_QUERY_SPAN = 3 * 60

integrationToken = ""
integrationEmail = ""
apiAccessToken = ""

def run():
    loadIntegrationToken()
    initializeRestApiWithIntegrationToken()
    running = True
    while running:
        queryRestApiForAuxSetting()
        time.sleep(MINIMUM_QUERY_SPAN)

def loadIntegrationToken():
    cfg = config.Config("pykinone.conf")
    if cfg:
        global integrationToken
        integrationToken = cfg['integrationToken']
        global integrationEmail
        integrationEmail = cfg['integrationEmail']
        print("Configuration file loaded...")
    else:
        print("Error loading config file")
    return

def initializeRestApiWithIntegrationToken():
    print("Initializing integration token with REST API...")
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': integrationToken
    }
    data = {
        'email': integrationEmail, 
        'integratorToken': integrationToken
    }
    r = requests.put(AUTH_TOKEN_ENDPOINT_URI_PATH, data=data, headers=headers)
    print(r.json())
    return

def queryRestApiForAuxSetting():
    print("Querying REST API...")
    return

run()