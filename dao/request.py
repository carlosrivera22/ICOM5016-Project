from config.db_config import pg_config
import psycopg2
class RequestData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select request_id, date_submited, resource_id from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedResources(self):
        cursor = self.conn.cursor()
        query = "select resource_name from request natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedResourcesByKeyword(self,keyword):
        cursor = self.conn.cursor()
        query = "select resource_name from request natural inner join resource where keyword = %s order by resource_name;"
        cursor.execute(query,(keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self,rid):
        cursor = self.conn.cursor()
        query = "select * from request where request_id = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getRequestsByVictimId(self,vid):
        cursor = self.conn.cursor()
        query = "select first_name, last_name, date_submited, resource_name, isFree from request natural inner join disaster_victim where victim_id = %s;"
        cursor.execute(query, (vid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByResourceId(self,resid):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join resource where resource_id = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, date_sumited, resource_id, victim_id):
        cursor = self.conn.cursor()
        query_1 = "insert into Request(date_sumited, resource_id) values (%s, %s) returning request_id;"
        cursor.execute(query_1, (date_sumited, resource_id))
        request_id = cursor.fetchone()[0]
        query_2 = "insert into RequestedBy(victim_id, request_id) values (%s, %s) returning requestedBy_id"
        cursor.execute(query_2, (victim_id, request_id))
        self.conn.commit()
        return request_id