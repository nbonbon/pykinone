class SwitchbotMeter:
    def __init__(self, time, address, rssi, batteryLife, temperature, temperatureUnit, humidity):
        self.time_utc = time
        self.address = address
        self.rssi = rssi
        self.batteryLife = batteryLife
        self.temperature = temperature
        self.temperatureUnit = temperatureUnit
        self.humidity = humidity
    
    def toString(self):
        result = "Time: " + self.time_utc + "\n"
        result += "\tAddress: " + self.address + "\n"
        result += "\tRSSI: " + self.rssi + "\n"
        result += "\tBattery: " + str(self.batteryLife) + "%\n"
        result += "\tTemp: " + str(self.temperature) + "\u00B0" + self.temperatureUnit + "\n"
        result += "\tHumidity: " + str(self.humidity) + "%\n"