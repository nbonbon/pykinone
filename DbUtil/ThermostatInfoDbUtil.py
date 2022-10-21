class ThermostatInfoDbUtil:
    def createThermostatInfoTable(self, curs):
        return curs.execute("""
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