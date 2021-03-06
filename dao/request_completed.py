from config.db_config import pg_config
import psycopg2
class RequestCompletedData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllRequestsCompleted(self):
        cursor = self.conn.cursor()
        query = "select * from request_completed;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByID(self, request_completed_id):
        cursor = self.conn.cursor()
        query = "select * from request_completed where request_completed_id = %s;"
        cursor.execute(query, (request_completed_id,))
        result = cursor.fetchone()
        return result

    def getRequestCompletedByDateResolved(self, date_resolved):
        cursor = self.conn.cursor()
        query = "select * from request_completed where date_resolved = %s;"
        cursor.execute(query, (date_resolved,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByOrderType(self, order_type):
        cursor = self.conn.cursor()
        query = "select * from order_type where order_type = %s;"
        cursor.execute(query, (order_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select request_completed_id, resource_name, date_resolved, price, order_type from request_completed natural inner join supplier natural inner join resource where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByVictimId(self, victim_id):
        cursor = self.conn.cursor()
        query = "select victim_id, company_name, resource_name, date_resolved, order_type, price, total from request_completed natural inner join disaster_victim natural inner join supplier natural inner join resource natural inner join supplies natural inner join account where victim_id = %s;"
        cursor.execute(query, (victim_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select request_completed_id, resource_name, price, quantity, total, date_resolved, order_type from request_completed natural inner join resource where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByCategoryId(self, category_id):
        cursor = self.conn.cursor()
        query = "select * from request_completed natural inner join category where category_id = %s;"
        cursor.execute(query, (category_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestCompletedByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from request_completed where price = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceNameFromRequestCompleted(self):
        cursor = self.conn.cursor()
        query = "select resource_name from request_completed natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSaleRequestCompletedByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select resource_name, date_resolved, price, company_name, victim_id from request_completed natural inner join resource natural inner join supplier where resource_id = %s and order_type = 'Sale';"
        cursor.execute(query, (resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionSaleRequestCompletedByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select request_completed_id, resource_name, date_resolved, price, company_name, victim_id from request_completed natural inner join resource natural inner join supplier where resource_id = %s and order_type = 'Sale';"
        cursor.execute(query, (resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertSale(self, date_resolved, supplier_id, victim_id, resource_id, price, quantity):
        cursor = self.conn.cursor()
        query_1 = "insert into request(date_submited, resource_id) values (%s, %s) returning request_id;"
        cursor.execute(query_1, (date_resolved, resource_id))
        request_id = cursor.fetchone()[0]
        query_2 = "insert into requestby( victim_id, request_id) values (%s, %s);"
        cursor.execute(query_2, (victim_id, request_id))
        query_get_quantity = "Select quantity from resource where resource_id = %s;"
        cursor.execute(query_get_quantity, (resource_id))
        actual_quantity = cursor.fetchone()[0]
        actual_quantity = int(actual_quantity)
        query_3 = "update resource set quantity = %s;"
        sub = actual_quantity - quantity
        sub = str(sub)
        cursor.execute(query_3, (sub,))
        query_4 = "insert into request_completed(request_id, date_resolved, order_type, supplier_id, victim_id, resource_id, price) values (%s, %s, 'Sale', %s, %s, %s, %s) returning request_completed_id;"
        cursor.execute(query_4, (request_id, date_resolved, supplier_id, victim_id, resource_id, (price * quantity)))
        request_completed_id = cursor.fetchone()[0]
        self.conn.commit()
        return request_completed_id


    def getAllSales(self):
        cursor = self.conn.cursor()
        query = "select * from request_completed where order_type = 'Sale';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertDonation(self, date_resolved, supplier_id, victim_id, resource_id, quantity,isavailable):
        cursor = self.conn.cursor()
        query_1 = "insert into request(date_submited, resource_id) values (%s, %s) returning request_id;"
        cursor.execute(query_1, (date_resolved, resource_id))
        print("done1")
        request_id = cursor.fetchone()[0]
        query_2 = "insert into requestby( victim_id, request_id) values (%s, %s);"
        cursor.execute(query_2, (victim_id, request_id))
        print("done2")
        query_3 = "update resource set quantity = %s, isavailable=%s where resource_id=%s;"
        cursor.execute(query_3, (quantity,isavailable,resource_id))
        print("done3")
        query_4 = "insert into request_completed(request_id, date_resolved, order_type, supplier_id, victim_id, resource_id, price) values (%s, %s, 'Donation', %s, %s, %s, %s) " \
                  "returning request_completed_id;"
        price = 0.00*float(quantity)
        cursor.execute(query_4, (request_id, date_resolved, supplier_id, victim_id, resource_id, price))
        request_completed_id = cursor.fetchone()[0]
        self.conn.commit()
        return request_completed_id

    def getAllDonation(self):
        cursor = self.conn.cursor()
        query = "select * from request_completed where order_type = 'Donation';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result



