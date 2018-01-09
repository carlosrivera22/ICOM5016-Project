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
        query = "select * from resource where resource_id = %s"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getAvailableResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource where isavailable = TRUE;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNeededResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource where isneeded = TRUE;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByName(self,resource_name):
        cursor = self.conn.cursor()
        query = "select * from resource where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = query.fetchone()
        return result

    def getResourcesByKeyword(self, keyword):
        cursor = self.conn.cursor()
        query = "select * from resource where keyword = %s;"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def getResourcesByKeywordAndAvailability(self, keyword, by_needed, by_available):
        cursor = self.conn.cursor()
        if(by_needed):
            query = "select * from resource where keyword = %s and isneeded = TRUE order by resource_name;"
        if (by_available):
            query = "select * from resource where keyword = %s and isavailable = TRUE order by resource_name;"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceCategory(self,resource_id):
        cursor = self.conn.cursor()
        query = "select category_name from resource natural inner join category where resource_nid = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getResourceSubCategory(self,resource_id):
        cursor = self.conn.cursor()
        query = "select category_name from resource natural inner join category natural inner join subcategory where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getResourceQuantity(self, name):
        cursor = self.conn.cursor()
        query = "select quantity from resource where resource_name = %s;"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        return result


