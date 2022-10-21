class LocationDbUtil:
    def createLocationTable(self, curs):
        return curs.execute("""
                CREATE TABLE location(
                    location_name TEXT PRIMARY KEY
                )
            """)
    
    def save(self, location, curs, con):
        if self.__locationExists(location, curs):
            return
        
        queryString = """
            INSERT into location VALUES
                ("{name}")
        """.format(name=location.name)
        curs.execute(queryString)
        return con.commit()

    def __locationExists(self, location, curs):
        queryString = """
            SELECT *  FROM location WHERE location_name = 
                ("{name}")
        """.format(name=location.name)
        res = curs.execute(queryString)
        if len(res.fetchone()) > 0:
            return True