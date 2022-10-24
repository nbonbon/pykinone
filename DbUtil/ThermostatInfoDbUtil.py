class ThermostatInfoDbUtil:
    def createThermostatInfoTable(self, curs):
        return curs.execute("""
            CREATE TABLE thermostat_info(
                timestamp DATETIME DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')),
                dev_id INTEGER,
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
                FOREIGN KEY(dev_id) REFERENCES device(device_id),
                PRIMARY KEY(timestamp, dev_id)
            )
        """)

    def save(self, thermostateInfo, curs, con):
        queryString = """
            INSERT into thermostat_info VALUES(
                datetime(CURRENT_TIMESTAMP, 'localtime'),
                "{dev_id}", 
                "{equipmentStatus}",
                "{mode}",
                "{modeLimit}",
                "{modeEmHeatAvailable}",
                "{fan}",
                "{fanCirculate}",
                "{fanCirculateSpeed}",
                "{heatSetpoint}",
                "{coolSetpoint}",
                "{setpointDelta}",
                "{setpointMinimum}",
                "{setpointMaximum}",
                "{tempIndoor}",
                "{humIndoor}",
                "{tempOutdoor}",
                "{humOutdoor}",
                "{scheduleEnabled}",
                "{geofencingEnabled}"
            )
        """.format(dev_id=thermostateInfo.deviceId, 
                    equipmentStatus=thermostateInfo.equipmentStatus,
                    mode=thermostateInfo.mode, 
                    modeLimit=thermostateInfo.modeLimit, 
                    modeEmHeatAvailable=thermostateInfo.modeEmHeatAvailable, 
                    fan=thermostateInfo.fan, 
                    fanCirculate=thermostateInfo.fanCirculate, 
                    fanCirculateSpeed=thermostateInfo.fanCirculateSpeed, 
                    heatSetpoint=thermostateInfo.heatSetpoint, 
                    coolSetpoint=thermostateInfo.coolSetpoint, 
                    setpointDelta=thermostateInfo.setpointDelta, 
                    setpointMinimum=thermostateInfo.setpointMinimum, 
                    setpointMaximum=thermostateInfo.setpointMaximum, 
                    tempIndoor=thermostateInfo.tempIndoor, 
                    humIndoor=thermostateInfo.humIndoor, 
                    tempOutdoor=thermostateInfo.tempOutdoor, 
                    humOutdoor=thermostateInfo.humOutdoor,
                    scheduleEnabled=thermostateInfo.scheduleEnabled,
                    geofencingEnabled=thermostateInfo.geofencingEnabled
        )
        curs.execute(queryString)
        return con.commit()