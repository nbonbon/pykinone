import threading
import logging
from datetime import datetime, timezone
from bluepy import btle 
from bluepy.btle import DefaultDelegate, ScanEntry
from ble.SwitchbotMeter import SwitchbotMeter
from Entity.TemperatureUnit import TemperatureUnit

 # TODO: Take this in as a param
logger = logging.getLogger('MainLogger')

class SwitchbotMeterScanner(DefaultDelegate):
    service_uuid = "cba20d00-224d-11e6-9fb8-0002a5d5c51b"

    def __init__(self, macs):
        btle.DefaultDelegate.__init__(self)
        self._lock = threading.Lock()
        self.meters = {}
        self.macs = macs
        self.TAG = self.__class__.__name__ + ":"

    def handleDiscovery(self, scanEntry, isNewDev, isNewData):
        if scanEntry.addr not in self.macs.values():
            return

        # self.is_switchbot(scanEntry) # TODO: Make work
        # self.is_switchbot_meter(scanEntry) # TODO: Make work

        for (tag, desc, val) in scanEntry.getScanData():
            if desc == '16b Service Data':
                service_data = scanEntry.getValue(ScanEntry.SERVICE_DATA_16B)
                temperature = (service_data[6] & 0b01111111) + (
                    (service_data[5] & 0b00001111) / 10
                ) 
                if not (service_data[6] & 0b10000000):  
                    temperature = -temperature
                if not (service_data[7] & 0b10000000):
                    tempUnits = TemperatureUnit.Celsius
                else:
                    tempUnits = TemperatureUnit.Fahrenheit
                    temperature = round(
                        temperature * 1.8 + 32, 1
                    ) 

                humidity = service_data[7] & 0b01111111
                battery = service_data[4] & 0b01111111
                utcTime = datetime.now(timezone.utc)

                with self._lock:
                    name = self.getDeviceName(scanEntry.addr)
                    meter = SwitchbotMeter(utcTime, scanEntry.addr, scanEntry.rssi, battery, temperature, tempUnits, humidity, name)
                    if meter is not None:
                        logger.debug(self.TAG + 'Updating meter: ' + name + ' [' + scanEntry.addr+ ']')
                        self.meters[scanEntry.addr] = meter 
                    else:
                        logger.debug(self.TAG + 'Meter was None!')

        if not scanEntry.scanData:
            logger.debug('(no data)')

    def getDeviceName(self, mac):
        if mac not in self.macs.values():
            return "None"
        else:
             return list(self.macs.keys())[list(self.macs.values()).index(mac)]

    def is_switchbot(self, scanEntry):
        services = scanEntry.getValue(ScanEntry.COMPLETE_128B_SERVICES)

        if (services and services[0] == self.service_uuid):
            logger.debug('* Found Switchbot device.')
            return True
        else:
            logger.debug('* Not a Switchbot device.')
            return False

    def is_switchbot_meter(self, scanEntry):
        service_data = scanEntry.getValue(ScanEntry.SERVICE_DATA_16B)

        if (service_data and len(service_data) == 8 and service_data[2] == 0x54):
            logger.debug('* Found Switchbot Meter.')
            return True
        else:
            logger.debug('* Not a Switchbot Meter.')
            return False

    def scanForSwitchbotMeters(self):
        while True:
            scanner = btle.Scanner().withDelegate(self)
            scanner.scan(10)

    def getMeters(self):
        with self._lock:
            return self.meters