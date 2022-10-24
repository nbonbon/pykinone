import sqlite3
from DbUtil.LocationDbUtil import LocationDbUtil
from DbUtil.DeviceDbUtil import DeviceDbUtil
from DbUtil.ThermostatInfoDbUtil import ThermostatInfoDbUtil
from Entity.Location import Location
from Entity.ThermostatInfo import ThermostatInfo

class DbManager:
    def __init__(self):
        self.con = sqlite3.connect("pykinone.db")
        self.con.execute("PRAGMA foreign_keys = 1")
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

    def save(self, object):
        if isinstance(object, Location):
            self.locationUtil.save(object, self.curs, self.con)
            for device in object.devices:
                self.deviceUtil.save(device, object, self.curs, self.con)
        elif isinstance(object, ThermostatInfo):
            self.thermostateInfoUtil.save(object, self.curs, self.con)