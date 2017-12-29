from config.db_config import pg_config
import psycopg2 

class UserData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    users = [
        {
            'user_id':1,
            'first_name':'Fernando',
            'last_name':'mercado',
            'email':'fmercado@email.com',
            'phone':'7870001111',
            'password':'pwd',
        },
        {
            'user_id':2,
            'first_name':'',
            'last_name':'',
            'email':'',
            'phone':'',
            'password':'',
        },
        {
            'user_id':3,
            'first_name':'',
            'last_name':'',
            'email':'',
            'phone':'',
            'password':'',
        }
    ]

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        print(result)
        return result
        #return self.users

    def getUserById(self,uid):
        for u in self.users:
            if u['user_id'] == uid:
                return u
        return 'No user found'

    def getUserByFirstName(self,fname):
        for u in self.user:
            if u['first_name'] == fname:
                return u
        return 'No user found'

    def getUserByLastName(self,lname):
        for u in self.user:
            if u['last_name'] == lname:
                return u
        return 'No user found'

    def getUserByFirstNameAndLastName(self,fname,lname):
        for u in self.user:
            if u['first_name'] == fname and u['last_name'] == lname:
                return u
        return 'No user found'

    def getUserByEmail(self,email):
        for u in self.user:
            if u['email'] == email:
                return u
        return 'No user found'

    def getUserByPhone(self,phone):
        for u in self.user:
            if u['phone'] == phone:
                return u
        return 'No user found'
