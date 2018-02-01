from config.db_config import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllSupplier(self):
        cursor = self.conn.cursor()
        query = "select supplier_id, first_name, last_name, email, phone, company_name, street, city, state, country, zipcode from account natural inner join" \
                " supplier natural inner join address ;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select supplier_id, first_name, last_name, email, phone, company_name, street, city, state, country, zipcode from account natural inner join supplier natural inner join address where supplier_id = %s ;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def getSupplierByFirstName(self, first_name):
        cursor = self.conn.cursor()
        query = "select supplier_id, first_name, last_name, email, phone, company_name, street, city, state, country, zipcode from account natural inner join" \
                "supplier natural inner join address where first_name = %s ;"
        cursor.execute(query, (first_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByLastName(self, last_name):
        cursor = self.conn.cursor()
        query = "select supplier_id, first_name, last_name, email, phone, company_name, street, city, state, country, zipcode from account natural inner join" \
                "supplier natural inner join address where last_name = %s ;"
        cursor.execute(query, (last_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select supplier_id, first_name, last_name, email, phone, company_name, street, city, state, country, zipcode from account natural inner join" \
                "supplier natural inner join address where email = %s ;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "select supplier_id, first_name, last_name, email, phone, company_name, street, city, state, country, zipcode from account natural inner join" \
                "supplier natural inner join address where phone = %s ;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByCompanyName(self, company_name):
        cursor = self.conn.cursor()
        query = "select supplier_id, first_name, last_name, email, phone, company_name, street, city, state, country, zipcode from account natural inner join" \
                "supplier natural inner join address where company_name = %s ;"
        cursor.execute(query, (company_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByAddressId(self, address_id):
        cursor = self.conn.cursor()
        query = "select supplier_id, first_name, last_name, email, phone, company_name, address_id, street, city, state, country, zipcode from account natural inner join" \
                "supplier natural inner join address where address_id = %s ;"
        cursor.execute(query, (address_id,))
        result = cursor.fetchone()
        return result

    def getAddressBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select address_id, street, city, state, country, zipcode from account natural inner join" \
                "supplier natural inner join address where supplier_id = %s ;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, category_id, resource_name, isavailable, isneeded, quantity, keyword from supplier natural inner join " \
                "supplies natural inner join resource where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRequestedCompletedBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select request_compledted_id, request_id, date_resolved, order_type, supplier_id, victim_id, resource_id, price from request_completed natural inner join supplier where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getSuppliersOfResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select first_name,last_name,company_name from account natural inner join supplier natural inner join supplies natural inner join resource where resource_id=%s;"
        cursor.execute(query,(resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByRegionId(self,region_id):
        cursor = self.conn.cursor()
        query = "select first_name, last_name, company_name, region_id from account natural inner join supplier natural inner join supplies natural inner join distribution_region where region_id = %s;"
        cursor.execute(query,(region_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result





    def insert(self, first_name, last_name, email, phone, password, confirm_password, company_name, street, region_id,
               city, state,
               country, zipcode):
        cursor = self.conn.cursor()
        query_1 = "insert into Account(first_name, last_name, email, phone, password, confirm_password) values (%s, %s, %s, %s, %s, %s) returning user_id;"
        cursor.execute(query_1, (first_name, last_name, email, phone, password, confirm_password))
        user_id = cursor.fetchone()[0]
        query_2 = "insert into Address(street, region_id, city, state, country, zipcode) values (%s, %s, %s, %s, %s, %s) returning address_id;"
        cursor.execute(query_2, (street, region_id, city, state, country, zipcode))
        address_id = cursor.fetchone()[0]
        query_3 = "insert into Supplier(user_id, address_id, company_name) values (%s, %s, %s) returning supplier_id;"
        cursor.execute(query_3, (user_id, address_id, company_name))
        supplier_id = cursor.fetchone()[0]
        self.conn.commit()
        return supplier_id
