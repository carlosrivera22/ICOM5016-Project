from config.db_config import pg_config
import psycopg2
class AddressData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllAddresses(self):
        cursor = self.conn.cursor()
        query = "select * from address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByRegion(self,region_name):
        cursor = self.conn.cursor()

    def getAddressesByCity(self,city):
        cursor = self.conn.cursor()

    def getAddressesByZipCode(self,zip_code):
        cursor = self.conn.cursor()

    def getAddressesByStreet(self,street):
        cursor = self.conn.cursor()

    def getAddressByUserId(self,user_id):
        cursor = self.conn.cursor()

