from config.db_config import pg_config
import psycopg2
class ResourceData:

    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesById(self,resource_id):
        cursor = self.conn.cursor()

    def getAvailableResources(self):
        cursor = self.conn.cursor()

    def getNeededResources(self):
        cursor = self.conn.cursor()

    def getResourcesByName(self,resource_name):
        cursor = self.conn.cursor()

    def getResourceCategory(self,resource_id):
        cursor = self.conn.cursor()

    def getResourceSubCategory(self,resource_id):
        cursor = self.conn.cursor()

