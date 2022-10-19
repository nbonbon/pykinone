class DeviceDbUtil:
    def createDeviceTable(self, curs):
        return curs.execute("""
                CREATE TABLE device(
                    device_id INTEGER PRIMARY KEY,
                    location_name TEXT,
                    device_name TEXT, 
                    model TEXT, 
                    firmware_version TEXT,
                    FOREIGN KEY(location_name) REFERENCES location(location_name)
                )
            """)