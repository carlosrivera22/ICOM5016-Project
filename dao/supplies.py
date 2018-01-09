from config.db_config import pg_config
import psycopg2
class SuppliesData:
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
        query = "select * from supplies natural inner join supplier where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliesByResourceId(self,resource_id):
        cursor = self.conn.cursor()
        query = "select * from supplies natural inner join resource where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getFreeSupplies(self):
        cursor = self.conn.cursor()
        query = "select * from Supplies where isFree = True;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNonFreeSupplies(self):
        cursor = self.conn.cursor()
        query = "select * from Supplies where isFree = False;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
