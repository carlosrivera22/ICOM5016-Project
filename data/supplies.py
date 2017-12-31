from config.db_config import pg_config
import psycopg2
class Supplies:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllSupplies(self):
        cursor = self.conn.cursor()
        query = "select * from supplies;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()

    def getSuppliesByResourceId(self,resource_id):
        cursor = self.conn.cursor()

    def getFreeSupplies(self):
        cursor = self.conn.cursor()

    def getNonFreeSupplies(self):
        cursor = self.conn.cursor()

