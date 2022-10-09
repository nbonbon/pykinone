import time
import config
import requests

DAIKIN_ONE_BASE_URI = "https://integrator-api.daikinskyport.com"
AUTH_TOKEN_ENDPOINT_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/token";
DEVICES_URI_PATH = DAIKIN_ONE_BASE_URI + "/v1/devices";
SECONDS_IN_ONE_MINUTE = 60
MINIMUM_QUERY_SPAN = 3 * 60

integrationToken = ""
integrationEmail = ""
apiAccessToken = ""

def run():
    integrationToken = loadIntegrationToken()
    apiAccessToken = initializeRestApiWithIntegrationToken()
    running = True
    while running:
        queryRestApiForAuxSetting()
        time.sleep(MINIMUM_QUERY_SPAN)

def loadIntegrationToken():
    cfg = config.Config("pykinone.conf")
    if cfg:
        integrationToken = cfg['integrationToken']
        integrationEmail = cfg['integrationEmail']
        print("Integration token read from configuration file")
        print("integration token: " + integrationToken)
        print("integration email: " + integrationEmail)
    else:
        print("Error loading config file")
    return

def initializeRestApiWithIntegrationToken():
    print("Initializing integration token with REST API...")
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': integrationToken
    }
    r = requests.put(AUTH_TOKEN_ENDPOINT_URI_PATH, data={"email": integrationEmail, "integratorToken": integrationToken}, headers=headers)
    print(r.json())
    return

def queryRestApiForAuxSetting():
    print("Querying REST API...")
    return

run()