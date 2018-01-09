from config.db_config import pg_config
import psycopg2
class DisasterVictimData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getVictimById(self,victim_id):
        cursor = self.conn.cursor()
        query = "select * from disaster_victim where victim_id = %s;"
        cursor.execute(query, (victim_id,))
        result = cursor.fetchone()
        return result

    def getVictimByUserId(self,user_id):
        cursor = self.conn.cursor()
        query = "select * from disaster_victim natural inner join user where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getVictimAddress(self,address_id):
        cursor = self.conn.cursor()
        query = "select * from disaster_victim natural inner join address where address_id = %s;"
        cursor.execute(query, (address_id,))
        result = cursor.fetchone()
        return result

    def getAllVictims(self):
        cursor = self.conn.cursor()
        query = "select * from disaster_victim;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedCompletedByVictimId(self, victim_id):
        cursor = self.conn.cursor()
        query = "select request_compledted_id, request_id, date_resolved, order_type, supplier_id, victim_id, resource_id, price from request_completed natural inner join disaster_victim where victim_id = %s;"
        cursor.execute(query, (victim_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedByVictimId(self, victim_id):
        cursor = self.conn.cursor()
        query = "select request_id, date_submited, resource_id from request natural inner join disaster_victim natural inner join requestby where victim_id = %s;"
        cursor.execute(query, (victim_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result