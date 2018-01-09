from config.db_config import pg_config
import psycopg2

class AddressDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllAddress(self):
        cursor = self.conn.cursor()
        query = "select * from address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressById(self, address_id):
        cursor = self.conn.cursor()
        query = "select * from address where address_id = %s;"
        cursor.execute(query, (address_id,))
        result = cursor.fetchone()
        return result

    def getAddressByStreet(self, street):
        cursor = self.conn.cursor()
        query = "select * from address where street = %s;"
        cursor.execute(query, (street,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByCity(self, city):
        cursor = self.conn.cursor()
        query = "select * from address where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByState(self, state):
        cursor = self.conn.cursor()
        query = "select * from address where state = %s;"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from address where country = %s;"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByZipcode(self, zipcode):
        cursor = self.conn.cursor()
        query = "select * from address where zipcode = %s;"
        cursor.execute(query, (zipcode,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByStreetAndCity(self, street, city):
        cursor = self.conn.cursor()
        query = "select * from address where street = %s and city = %s;"
        cursor.execute(query, (street,city))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByStreetAndState(self, street, state):
        cursor = self.conn.cursor()
        query = "select * from address where street = %s and state = %s;"
        cursor.execute(query, (street, state))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByStreetAndCountry(self, street, country):
        cursor = self.conn.cursor()
        query = "select * from address where street = %s and country = %s;"
        cursor.execute(query, (street, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByStreetAndZipcode(self, street, zipcode):
        cursor = self.conn.cursor()
        query = "select * from address where street = %s and zipcode = %s;"
        cursor.execute(query, (street, zipcode))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByCityAndState(self, city, state):
        cursor = self.conn.cursor()
        query = "select * from address where city = %s and state = %s;"
        cursor.execute(query, (city, state))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByCityAndCountry(self, city, country):
        cursor = self.conn.cursor()
        query = "select * from address where city = %s and country = %s;"
        cursor.execute(query, (city, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByCityAndZipcode(self, city, zipcode):
        cursor = self.conn.cursor()
        query = "select * from address where city = %s and zipcode = %s;"
        cursor.execute(query, (city, zipcode))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByStateAndCountry(self, state, country):
        cursor = self.conn.cursor()
        query = "select * from address where state = %s and country = %s;"
        cursor.execute(query, (state, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByStateAndZipcode(self, state, zipcode):
        cursor = self.conn.cursor()
        query = "select * from address where state = %s and zipcode = %s;"
        cursor.execute(query, (state, zipcode))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressByCountryAndZipcode(self, country, zipcode):
        cursor = self.conn.cursor()
        query = "select * from address where country = %s and zipcode = %s;"
        cursor.execute(query, (country, zipcode))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRegionByAddressId(self, address_id):
        cursor = self.conn.cursor()
        query = "select region_id, region_name, region_number from address natural inner join region where address_id = %s;"
        cursor.execute(query, (address_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result