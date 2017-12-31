from config.db_config import pg_config
import psycopg2

class SupplierData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        print(result)
        return result

    def getSupplierById(self,sid):
        cursor = self.conn.cursor()

    def getSuppliersByAddress(self,address_id):
        cursor = self.conn.cursor()






