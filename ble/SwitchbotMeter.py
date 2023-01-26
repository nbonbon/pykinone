from datetime import datetime

class SwitchbotMeter:
    def __init__(self, time, address, rssi, batteryLife, temperature, temperatureUnit, humidity, name):
        self.time_utc = time
        self.address = address
        self.rssi = rssi
        self.batteryLife = batteryLife
        self.temperature = temperature
        self.temperatureUnit = temperatureUnit
        self.humidity = humidity
        self.name = name
    
    def toString(self):
        result = "\tTime: " + self.time_utc.isoformat(" ","seconds") + "\n"
        result += "\tName: " + self.name + "\n"
        result += "\tAddress: " + self.address + "\n"
        result += "\tRSSI: " + str(self.rssi) + " dBm\n"
        result += "\tBattery: " + str(self.batteryLife) + "%\n"
        result += "\tTemp: " + str(self.temperature) + "\u00B0 " + self.temperatureUnit.upper() + "\n"
        result += "\tHumidity: " + str(self.humidity) + "%\n"
        return result