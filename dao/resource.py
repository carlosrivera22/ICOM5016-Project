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
        query = "select * from resource where resource_id = %s;"
        cursor.execute(query,(resource_id,))
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


    #GET FREE RESOURCES
    def getFreeResources(self):
        cursor = self.conn.cursor()
        query = "select resource_id, category_id, resource_name, isavailable, isneeded, quantity, keyword from resource natural inner join supplies where isfree= TRUE;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Tienes que escoger un suplidor
    # Categoria tiene que existir en la base de datos
    # Subcategoria tiene que existir en la base de datos (opcional)
    def insert(self, category_id, resource_name, quantity, keyword, subcategory_id, supplier_id, price):
        cursor = self.conn.cursor()
        isneeded = False
        if quantity > 0:
            isavailable = True
        else:
            isavailable = False
        if price > 0:
            isfree = False
        else:
            isfree = True
        query_1 = "insert into Resource(category_id, resource_name, isavailable, isneeded, quantity, keyword, subcategory_id) values (%s, %s, %s, %s, %s, %s, %s) returning resource_id;"
        cursor.execute(query_1, (category_id, resource_name, isavailable, isneeded, quantity, keyword, subcategory_id))
        resource_id = cursor.fetchone()[0]
        print(resource_id)
        query_2 = "insert into Supplies(supplier_id, resource_id, price, isfree) values (%s, %s, %s, %s) returning supplies_id"
        cursor.execute(query_2, (supplier_id, resource_id, price, isfree))
        supplies_id = cursor.fetchone()[0]
        print(supplier_id)
        self.conn.commit()
        return resource_id

    def update(self, resource_id, category_id, resource_name, isavailable, isneeded, quantity, keyword, subcategory_id, supplier_id, price, isfree):
        cursor = self.conn.cursor()
        query_1 = "update resource set category_id = %s, resource_name = %s, isavailable = %s, isneeded = %s, quantity = %s, keyword = %s, subcategory_id = %s where resource_id=%s;"
        cursor.execute(query_1, (category_id, resource_name, isavailable, isneeded, quantity, keyword, subcategory_id, resource_id))
        query_2 = "update supplies set supplier_id = %s, resource_id =%s, price = %s, isfree = %s where resource_id = %s;"
        cursor.execute(query_2, (supplier_id, resource_id, price, isfree, resource_id))
        self.conn.commit()
        return resource_id
#Annoucement DAO methods....................................................................................................................................................
    def getAllAnnouncement(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, resource_name, quantity, price, isavailable, first_name, last_name, company_name from resource natural inner join announcement natural inner join supplies natural inner join account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, resource_name, quantity, price, isavailable, first_name, last_name, company_name from resource natural inner join announcement natural inner join supplies natural inner join account where resource_id = %s;"
        cursor.execute(query, (resource_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertAnnouncement(self,resource_id):
        cursor = self.conn.cursor()
        query = "insert into announcement(resource_id) values (%s) returning annoucement_id;"
        cursor.execute(query,(resource_id))
        annoucement_id = cursor.fetchone()[0]
        self.conn.commit()
        return annoucement_id

   

