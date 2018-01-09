from config.db_config import pg_config
import psycopg2

class BankAccountDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllBankAccount(self):
        cursor = self.conn.cursor()
        query = "select * from bank_account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountById(self, bank_account_id):
        cursor = self.conn.cursor()
        query = "select * from bank_account where bank_account = %s;"
        cursor.execute(query, (bank_account_id,))
        result = cursor.fetchone()
        return result

    def getBankAccountByBankAccountNo(self, bank_account_no):
        cursor = self.conn.cursor()
        query = "select * from bank_account where bank_account_no = %s;"
        cursor.execute(query, (bank_account_no,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByAccountType(self, bank_account_type):
        cursor = self.conn.cursor()
        query = "select * from bank_account where bank_account_type = %s;"
        cursor.execute(query, (bank_account_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByAmount(self, amount):
        cursor = self.conn.cursor()
        query = "select * from bank_account where amount = %s;"
        cursor.execute(query, (amount,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select bank_account_id, bank_account_no, bank_account_type, amount, supplier_id from bank_account natural inner join supplier where supplier_id =%s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByBankAccountId(self, bank_account_id):
        pass

