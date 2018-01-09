from flask import jsonify
from dao.address import AddressDAO


class AddressHandler:

    def build_address_dict(self, row):
        result = {}
        result['address_id'] = row[0]
        result['region_id'] = row[1]
        result['street'] = row[2]
        result['city'] = row[3]
        result['state'] = row[4]
        result['country'] = row[5]
        result['zipcode'] = row[6]
        return result

    def build_region_dict(self, row):
        result = {}
        result['region_id'] = row[0]
        result['region_name'] = row[1]
        result['region_number'] = row[2]
        return result


    def build_address_attributes(self, address_id, region_id, street, city, state, country, zipcode):
        result = {}
        result['address_id'] = address_id
        result['region_id'] = region_id
        result['street'] = street
        result['city'] = city
        result['state'] = state
        result['country'] = country
        result['zipcode'] = zipcode
        return result

    def getAllAddrees(self):
        dao = AddressDAO()
        address_list = dao.getAllAddress()
        result_list = []
        for row in address_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Address=result_list)


    def getAddressById(self, address_id):
        dao = AddressDAO()
        row = dao.getAddressById(address_id)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address=address)

    def getRegionByAddresId(self, address_id):
        dao = AddressDAO()
        if not dao.getAddressById(address_id):
            return jsonify(Error="Address Not Found"), 404
        regions_list = dao.getRegionByAddressId(address_id)
        result_list = []
        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Regions=result_list)

    def searchAddress(self, args):
        street = args.get("street")
        city = args.get("city")
        state = args.get("state")
        country = args.get("country")
        zipcode = args.get("zipcode")
        dao = AddressDAO()
        address_list = []

        if (len(args) == 1) and street:
            address_list = dao.getAddressByStreet(street)
        elif (len(args) == 1) and city:
            address_list = dao.getAddressByCity(city)
        elif (len(args) == 1) and state:
            address_list = dao.getAddressByState(state)
        elif (len(args) == 1) and country:
            address_list = dao.getAddressByCountry(country)
        elif (len(args) == 1) and zipcode:
            address_list = dao.getAddressByZipcode(zipcode)
        elif (len(args) == 2) and street and city:
            address_list = dao.getAddressByStreetAndCity(street, city)
        elif (len(args) == 2) and street and state:
            address_list = dao.getAddressByStreetAndState(street, state)
        elif (len(args) == 2) and street and country:
            address_list = dao.getAddressByStreetAndCountry(street, country)
        elif (len(args) == 2) and street and zipcode:
            address_list = dao.getAddressByStreetAndZipcode(street, zipcode)
        elif (len(args) == 2) and city and state:
            address_list = dao.getAddressByCityAndState(city, state)
        elif (len(args) == 2) and city and country:
            address_list = dao.getAddressByCityAndCountry(city, country)
        elif (len(args) == 2) and city and zipcode:
            address_list = dao.getAddressByCityAndZipcode()(city, zipcode)
        elif (len(args) == 2) and state and country:
            address_list = dao.getAddressByStateAndCountry()(state, country)
        elif (len(args) == 2) and state and zipcode:
            address_list = dao.getAddressByStateAndZipcode(state, zipcode)
        elif (len(args) == 2) and country and zipcode:
            address_list = dao.getAddressByCountryAndZipcode(country, zipcode)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in address_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Address=result_list)
