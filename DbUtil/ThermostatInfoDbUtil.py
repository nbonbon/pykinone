from Entity.ThermostatInfo import ThermostatInfo


class ThermostatInfoDbUtil:
    def createThermostatInfoTable(self, curs):
        return curs.execute("""
            CREATE TABLE thermostat_info(
                timestamp DATETIME DEFAULT (datetime(CURRENT_TIMESTAMP, 'utc')),
                dev_id TEXT,
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

    def save(self, thermostatInfo, curs, con):
        if self.__hasDataUpdatedSinceLastSave(thermostatInfo, curs) == False:
            return

        queryString = """
            INSERT into thermostat_info VALUES(
                datetime(CURRENT_TIMESTAMP, 'utc'),
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
        """.format(dev_id=thermostatInfo.deviceId, 
                    equipmentStatus=thermostatInfo.equipmentStatus,
                    mode=thermostatInfo.mode, 
                    modeLimit=thermostatInfo.modeLimit, 
                    modeEmHeatAvailable=thermostatInfo.modeEmHeatAvailable, 
                    fan=thermostatInfo.fan, 
                    fanCirculate=thermostatInfo.fanCirculate, 
                    fanCirculateSpeed=thermostatInfo.fanCirculateSpeed, 
                    heatSetpoint=thermostatInfo.heatSetpoint, 
                    coolSetpoint=thermostatInfo.coolSetpoint, 
                    setpointDelta=thermostatInfo.setpointDelta, 
                    setpointMinimum=thermostatInfo.setpointMinimum, 
                    setpointMaximum=thermostatInfo.setpointMaximum, 
                    tempIndoor=thermostatInfo.tempIndoor, 
                    humIndoor=thermostatInfo.humIndoor, 
                    tempOutdoor=thermostatInfo.tempOutdoor, 
                    humOutdoor=thermostatInfo.humOutdoor,
                    scheduleEnabled=(1 if thermostatInfo.scheduleEnabled == True else 0),
                    geofencingEnabled=(1 if thermostatInfo.geofencingEnabled == True else 0)
        )
        curs.execute(queryString)
        return con.commit()

    def __hasDataUpdatedSinceLastSave(self, thermostatInfo, curs):
        queryString = """
            SELECT * FROM thermostat_info 
            WHERE dev_id = "{dev_id}"
            ORDER BY timestamp DESC
            LIMIT 1
        """.format(dev_id=thermostatInfo.deviceId)
        res = curs.execute(queryString)
        if res is not None:
            res = res.fetchone()
            if res is not None:
                oldInfo = ThermostatInfo()

                oldInfo.deviceId=res[1]
                oldInfo.equipmentStatus=res[2]
                oldInfo.modeLimit=res[4]
                oldInfo.mode=res[3]
                oldInfo.fan=res[6]
                oldInfo.modeEmHeatAvailable=res[5]
                oldInfo.fanCirculate=res[7]
                oldInfo.fanCirculateSpeed=res[8]
                oldInfo.heatSetpoint=res[9]
                oldInfo.coolSetpoint=res[10]
                oldInfo.setpointDelta=res[11]
                oldInfo.setpointMinimum=res[12]
                oldInfo.setpointMaximum=res[13]
                oldInfo.tempIndoor=res[14]
                oldInfo.humIndoor=res[15]
                oldInfo.tempOutdoor=res[16]
                oldInfo.humOutdoor=res[17]
                oldInfo.scheduleEnabled=bool(res[18])
                oldInfo.geofencingEnabled=bool(res[19])
                    
                if oldInfo == thermostatInfo:
                    return False
        return True