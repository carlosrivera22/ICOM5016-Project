from config.db_config import pg_config
import psycopg2
class SubCategoryData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    #funciona
    def getAllSubcategories(self):
        cursor = self.conn.cursor()
        query = "select * from subcategory;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #funciona
    def getSubCategoryByCategoryId(self,category_id):
        cursor = self.conn.cursor()
        query = "select * from subcategory where category_id=%s;"
        cursor.execute(query,(category_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #funciona
    def getSubCategoryById(self,sub_cat_id):
        cursor = self.conn.cursor()
        query = "select * from subcategory where subcategory_id=%s;"
        cursor.execute(query,(sub_cat_id,))
        result = cursor.fetchone()
        return result

    #funciona
    def getCategoryFromSubcategoryId(self,sub_cat_id):
        cursor = self.conn.cursor()
        query = "select category_id,category_name from subcategory natural inner join category where sub_cat_id=%s;"
        cursor.execute(query,(sub_cat_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result







