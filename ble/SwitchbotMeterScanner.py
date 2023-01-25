import threading
import os
from datetime import datetime, timezone
from bluepy import btle 
from bluepy.btle import DefaultDelegate, ScanEntry
from ble.SwitchbotMeter import SwitchbotMeter
from Entity.TemperatureUnit import TemperatureUnit
from Util.TimeUtil import TimeUtil

METER_MACS = ['d2:51:27:12:fd:83','df:4a:2e:82:79:32'] # TODO: Take this in as a param
debug_level = 1 # TODO: Tie into existing logging

class SwitchbotMeterScanner(DefaultDelegate):
    service_uuid = "cba20d00-224d-11e6-9fb8-0002a5d5c51b"
    

    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        self._lock = threading.Lock()
        self.meters = {}

    def handleDiscovery(self, scanEntry, isNewDev, isNewData):
        if scanEntry.addr not in METER_MACS:
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
                utcTime = datetime.datetime.now(timezone.utc)

                with self._lock:
                    self.meters[scanEntry.addr] = SwitchbotMeter(utcTime, scanEntry.addr, scanEntry.rssi, battery, temperature, tempUnits, humidity)

        if not scanEntry.scanData:
            print ('\t(no data)')

    def is_switchbot(self, scanEntry):
        services = scanEntry.getValue(ScanEntry.COMPLETE_128B_SERVICES)

        if (services and services[0] == self.service_uuid):
            print('* Found Switchbot device.')
            return True
        else:
            print('* Not a Switchbot device.')
            return False

    def is_switchbot_meter(self, scanEntry):
        service_data = scanEntry.getValue(ScanEntry.SERVICE_DATA_16B)

        if (service_data and len(service_data) == 8 and service_data[2] == 0x54):
            print('* Found Switchbot Meter.')
            return True
        else:
            print('* Not a Switchbot Meter.')
            return False

    def scanForSwitchbotMeters(self):
        scanner = btle.Scanner().withDelegate(SwitchbotMeterScanner())
        scanner.scan(10)

    def getMeters(self):
        with self._lock:
            return self.meters