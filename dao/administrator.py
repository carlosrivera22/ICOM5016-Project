from config.db_config import pg_config
import psycopg2
class AdminData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    #funciona
    def getAdministratorById(self,administrator_id):
        cursor = self.conn.cursor()
        query = "select * from administrator where admin_id = %s;"
        cursor.execute(query,(administrator_id,))
        result = cursor.fetchone()
        return result

    #funciona
    def getAllAdministrators(self):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, password from administrator natural inner join account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #funciona
    def getUserByAdministratorId(self,admin_id):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, password from administrator natural join account where admin_id=%s;"
        cursor.execute(query,(admin_id,))
        result = cursor.fetchone()
        return result




        

