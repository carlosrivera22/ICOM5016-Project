from config.db_config import pg_config
import psycopg2
class RegionData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllRegions(self):
        cursor = self.conn.cursor()
        query = "select * from region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRegionByName(self,region_name):
        cursor = self.conn.cursor()

    def getRegionByNumber(self,region_number):
        cursor = self.conn.cursor()

