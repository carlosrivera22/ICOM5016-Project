from config.db_config import pg_config
import psycopg2

class UserDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUserId(self,user_id):
        cursor = self.conn.cursor()
        query = "select * from Account where user_id =%s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getUserByFirstName(self, first_name):
        cursor = self.conn.cursor()
        query = "select * from Account where first_name = %s;"
        cursor.execute(query, (first_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByLastName(self, last_name):
        cursor = self.conn.cursor()
        query = "select * from Account where last_name = %s;"
        cursor.execute(query, (last_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * from Account where email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "select * from Account where phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByFirstNameAndLastName(self, first_name, last_name):
        cursor = self.conn.cursor()
        query = "select * from Account where first_name = %s and last_name = %s;"
        cursor.execute(query, (first_name, last_name))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByEmailAndPhone(self, email, phone):
        cursor = self.conn.cursor()
        query = "select * from Account where email = %s and phone = %s;"
        cursor.execute(query, (email, phone))
        result = []
        for row in cursor:
            result.append(row)
        return result


