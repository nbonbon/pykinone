class LocationDbUtil:
    def createLocationTable(self, curs):
        return curs.execute("""
                CREATE TABLE location(
                    location_name TEXT PRIMARY KEY
                )
            """)
    
    def save(self, location, curs, con):
        queryString = """
            INSERT into location VALUES
                ("{name}")
        """.format(name=location.name)
        print("querystr: " + queryString)
        curs.execute(queryString)
        return con.commit()