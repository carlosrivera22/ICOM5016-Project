from config.db_config import pg_config
import psycopg2
class CategoryData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    #funciona
    def getAllCategories(self):
        cursor = self.conn.cursor()
        query = "select * from category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #funciona
    def getSubcategoriesFromCategoryId(self,category_id):
        cursor = self.conn.cursor()
        query = "select subcategory_id,subcategory_name,category_id from category natural inner join subcategory where category_id=%s;"
        cursor.execute(query,(category_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #funciona
    def getCategoryById(self,category_id):
        cursor = self.conn.cursor()
        query = "select * from category where category_id=%s;"
        cursor.execute(query,(category_id,))
        result = cursor.fetchone()
        return result

    #funciona
    def getCategoryByName(self,category_name):
        cursor = self.conn.cursor()
        query = "select * from category where category_name=%s;"
        cursor.execute(query,(category_name,))
        result = cursor.fetchone()
        return result





