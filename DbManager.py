import sqlite3
from LocationDbUtil import LocationDbUtil
from DeviceDbUtil import DeviceDbUtil

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
        if self.__tableExists("location") is False:
            print("Creating location table...")
            self.locationUtil.createLocationTable(self.curs)
        if self.__tableExists("device") is False:
            print("Creating device table...")
            self.deviceUtil.createDeviceTable(self.curs)
        if self.__tableExists("thermostat_info") is False:
            print("Creating thermostat_info table...")
            self.__createThermostatInfoTable()

    def __tableExists(self, tableName):
        res = self.curs.execute("SELECT name FROM sqlite_master WHERE  type='table' AND name='" + tableName +"'");
        return res.fetchone() is not None

    def __createThermostatInfoTable(self):
        return self.curs.execute("""
            CREATE TABLE thermostat_info(
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                info_device INTEGER,
                equipmentStatus INTEGER,
                mode INTEGER,
                modeLimit INTEGER,
                modeEmHeatAvailable INTEGER,
                fan INTEGER,
                fanCirculate INTEGER,
                fanCirculateSpeed INTEGER,
                heatSetpoint FLOAT,
                coolSetpoint FLOAT,
                setpointDelta FLOAT,
                setpointMinimum FLOAT,
                setpointMaximum FLOAT,
                tempIndoor FLOAT,
                humIndoor FLOAT,
                tempOutdoor FLOAT,
                humOutdoor FLOAT,
                scheduleEnabled INTEGER,
                geofencingEnabled INTEGER,
                FOREIGN KEY(info_device) REFERENCES device(device_id),
                PRIMARY KEY(timestamp, info_device)
            )
        """)