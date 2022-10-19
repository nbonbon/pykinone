import sqlite3
from LocationDbUtil import LocationDbUtil
from DeviceDbUtil import DeviceDbUtil
from ThermostatInfoDbUtil import ThermostatInfoDbUtil

class DbManager:
    def __init__(self):
        self.con = sqlite3.connect("pykinone.db")
        self.curs = self.con.cursor()
        self.__initializeTables()
    
    def close(self):
        self.con.close()

    def __initializeTables(self):
        self.locationUtil = LocationDbUtil()
        self.deviceUtil = DeviceDbUtil()
        self.thermostateInfoUtil = ThermostatInfoDbUtil()
        if self.__tableExists("location") is False:
            print("Creating location table...")
            self.locationUtil.createLocationTable(self.curs)
        if self.__tableExists("device") is False:
            print("Creating device table...")
            self.deviceUtil.createDeviceTable(self.curs)
        if self.__tableExists("thermostat_info") is False:
            print("Creating thermostat_info table...")
            self.thermostateInfoUtil.createThermostatInfoTable(self.curs)

    def __tableExists(self, tableName):
        res = self.curs.execute("SELECT name FROM sqlite_master WHERE  type='table' AND name='" + tableName +"'");
        return res.fetchone() is not None