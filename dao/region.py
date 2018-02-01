from config.db_config import pg_config
import psycopg2

class RegionDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRegion(self):
        cursor = self.conn.cursor()
        query = "select * from region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRegionById(self, region_id):
        cursor = self.conn.cursor()
        query = "select * from region where region_id = %s;"
        cursor.execute(query, (region_id,))
        result = cursor.fetchone()
        return result

    def getRegionByRegionName(self, region_name):
        cursor = self.conn.cursor()
        query = "select * from region where region_name = %s;"
        cursor.execute(query, (region_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRegionByRegionNumber(self, region_number):
        cursor = self.conn.cursor()
        query = "select * from region where region_number = %s;"
        cursor.execute(query, (region_number,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRegionByRegionNameAndRegionNumber(self, region_name, region_number):
        cursor = self.conn.cursor()
        query = "select * from region where region_name = %s and region_number = %s;"
        cursor.execute(query, (region_name, region_number))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByRegionId(self, region_id):
        cursor = self.conn.cursor()
        query = "select address_id, street, city, state, country, zipcode from region natural inner join address;"
        cursor.execute(query, (region_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

   
