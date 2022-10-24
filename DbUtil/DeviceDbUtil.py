class DeviceDbUtil:
    def createDeviceTable(self, curs):
        return curs.execute("""
                CREATE TABLE device(
                    device_id TEXT PRIMARY KEY,
                    location_name TEXT,
                    device_name TEXT, 
                    model TEXT, 
                    firmware_version TEXT,
                    FOREIGN KEY(location_name) REFERENCES location(location_name)
                )
            """)

    def save(self, device, location, curs, con):
        if self.__deviceExists(device, curs):
            return
        
        queryString = """
            INSERT into device VALUES
                ("{id}", "{loc_name}", "{dev_name}", "{model}", "{firmwareVersion}")
        """.format(id=device.id, loc_name=location.name, dev_name=device.name, model=device.model, firmwareVersion=device.firmwareVersion)
        curs.execute(queryString)
        return con.commit()

    def __deviceExists(self, device, curs):
        queryString = """
            SELECT *  FROM device WHERE device_id = 
                ("{id}")
        """.format(id=device.id)
        res = curs.execute(queryString)
        if res is not None:
            res = res.fetchone()
            if res is not None and len(res) > 0:
                return True
        return False