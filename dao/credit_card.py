from config.db_config import pg_config
import psycopg2

class CreditCardData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllCreditCards(self):
        cursor = self.conn.cursor()
        query = "select * from credit_card;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getCreditCardByVictimId(self,victim_id):
        cursor = self.conn.cursor()
        query = "select * from credit_card where victim_id=%s;"
        cursor.execute(query,(victim_id,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getCreditCardByNameOnCard(self,full_name):
        cursor = self.conn.cursor()
        query = "select * from credit_card where name_on_card=%s;"
        cursor.execute(query,(full_name,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result


    def getCreditCardByCreditCardNumber(self,credit_card_number):
        cursor = self.conn.cursor()
        query = "select * from credit_card where credit_card_number=%s;"
        cursor.execute(query,(credit_card_number,))
        result = cursor.fetchone()
        return result


    def getCreditCardById(self, credit_card_id):
        cursor = self.conn.cursor()
        query = "select * from credit_card where credit_card_id=%s;"
        cursor.execute(query,(credit_card_id,))
        result = cursor.fetchone()
        return result


    def getCreditCardByCVS(self,cvs):
        cursor = self.conn.cursor()
        query = "select * from credit_card where cvs=%s;"
        cursor.execute(query,(cvs,))
        result = cursor.fetchone()
        return result

    def getCreditCardByExpDate(self,exp_date):
        cursor = self.conn.cursor()
        query = "select * from credit_card where exp_date=%s;"
        cursor.execute(query,(exp_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getVictimByCreditCardNumber(self,credit_card_number):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, password from credit_card natural inner join disaster_victim natural inner join account where credit_card_number=%s;"
        cursor.execute(query,(credit_card_number,))
        result = cursor.fetchone()
        return result

    def getVictimByCreditCardId(self,credit_card_id):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, password from credit_card natural inner join disaster_victim natural inner join account where credit_card_id=%s;"
        cursor.execute(query,(credit_card_id,))
        result = cursor.fetchone()
        return result

    def getVictimByCreditCardCVS(self,cvs):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, password from credit_card natural inner join disaster_victim natural inner join account where cvs=%s;"
        cursor.execute(query,(cvs,))
        result = cursor.fetchone()
        return result

    def getVictimByNameOnCard(self,name_on_card):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, password from credit_card natural inner join disaster_victim natural inner join account where name_on_card=%s;"
        cursor.execute(query,(name_on_card,))
        result = cursor.fetchone()
        return result

    def getVictimsByCreditCardExpDate(self,exp_date):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, password from credit_card natural inner join disaster_victim natural inner join account where exp_date=%s;"
        cursor.execute(query,(exp_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result



