from config.db_config import pg_config
import psycopg2
class BankAccountData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllAccounts(self):
        cursor = self.conn.cursor()
        query = "select * from account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsBySupplierId(self,supplier_id):
        cursor = self.conn.cursor()

    def getAccountByNumber(self,account_number):
        cursor = self.conn.cursor()

    def getAccountById(self,account_id):
        cursor = self.conn.cursor()
