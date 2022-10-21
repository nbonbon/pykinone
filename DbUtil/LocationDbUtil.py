class LocationDbUtil:
    def createLocationTable(self, curs):
        return curs.execute("""
                CREATE TABLE location(
                    location_name TEXT PRIMARY KEY
                )
            """)