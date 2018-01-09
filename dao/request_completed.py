from config.db_config import pg_config
import psycopg2
class RequestCompletedData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllRequestsCompleted(self):
        cursor = self.conn.cursor()
        query = "select * from request_completed;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByID(self, request_completed_id):
        cursor = self.conn.cursor()
        query = "select * from request_completed where request_completed_id = %s;"
        cursor.execute(query, (request_completed_id,))
        result = cursor.fetchone()
        return result

    def getRequestCompletedByDateResolved(self, date_resolved):
        cursor = self.conn.cursor()
        query = "select * from request_completed where date_resolved = %s;"
        cursor.execute(query, (date_resolved,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByOrderType(self, order_type):
        cursor = self.conn.cursor()
        query = "select * from order_type where order_type = %s;"
        cursor.execute(query, (order_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_name, date_resolved, price, order_type from request_completed natural inner join supplier natural inner join resource where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByVictimId(self, victim_id):
        cursor = self.conn.cursor()
        query = "select * from request_completed natural inner join disaster_victim where victim_id = %s;"
        cursor.execute(query, (victim_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select * from request_completed natural inner join resource where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByCategoryId(self, category_id):
        cursor = self.conn.cursor()
        query = "select * from request_completed natural inner join category where category_id = %s;"
        cursor.execute(query, (category_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from request_completed where price = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result
