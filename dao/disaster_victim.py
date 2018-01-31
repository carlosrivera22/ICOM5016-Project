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

    def getVictimInfoById(self, victim_id):
        cursor = self.conn.cursor()
        query = "select victim_id, first_name, last_name, street, city, state, country, zipcode from disaster_victim natural inner join account natural inner join address where victim_id = %s;"
        cursor.execute(query, (victim_id,))
        result = cursor.fetchone()
        return result

    def getVictimByUserId(self,user_id):
        cursor = self.conn.cursor()
        query = "select * from disaster_victim natural inner join account where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getVictimAddress(self,address_id):
        cursor = self.conn.cursor()
        query = "select * from disaster_victim natural inner join address where address_id = %s;"
        cursor.execute(query, (address_id,))
        result = cursor.fetchone()
        return result

    def getVictimCreditCard(self, victim_id):
        cursor = self.conn.cursor()
        query = "select first_name, last_name, victim_id, name_on_card, credit_card_number, exp_date, cvs from disaster_victim natural inner join account natural inner join credit_card where victim_id = %s"
        cursor.execute(query,(victim_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllVictims(self):
        cursor = self.conn.cursor()
        query = "select * from disaster_victim;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllVictimsInfo(self):
        cursor = self.conn.cursor()
        query = "select victim_id, first_name, last_name, street, city, state, country, zipcode from disaster_victim natural inner join account natural inner join address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        print(row)
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
        query = "select * from request natural inner join requestby natural inner join resource natural inner join disaster_victim where victim_id=%s;"
        cursor.execute(query, (victim_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, first_name, last_name, email, phone, password, confirm_password, street, region_id, city, state,
               country, zipcode):
        cursor = self.conn.cursor()
        query_1 = "insert into Account(first_name, last_name, email, phone, password, confirm_password) values (%s, %s, %s, %s, %s, %s) returning user_id;"
        cursor.execute(query_1, (first_name, last_name, email, phone, password, confirm_password))
        user_id = cursor.fetchone()[0]
        print(user_id)
        query_2 = "insert into Address(street, region_id, city, state, country, zipcode) values (%s, %s, %s, %s, %s, %s) returning address_id;"
        cursor.execute(query_2, (street, region_id, city, state, country, zipcode))
        address_id = cursor.fetchone()[0]
        print(address_id)
        query_3 = "insert into disaster_victim(user_id, address_id) values (%s, %s) returning victim_id;"
        cursor.execute(query_3, (user_id, address_id,))
        victim_id = cursor.fetchone()[0]
        print(victim_id)
        self.conn.commit()
        return victim_id
