from flask import jsonify
from data.address import AddressData

class AddressHandler:

    def getAllAddresses(self):
        address_data = AddressData()
        return jsonify(address_data.getAllAdresses())

    def getAddressById(self,aid):
        address_data = AddressData()
        return jsonify(address_data.getAddressById(aid))

    def getAddressOfUserByUserId(self,uid):
        address_data = AddressData()
        return jsonify(address_data.getAddressOfUserByUserId(uid))

    def getAllAddressesOfARegion(self,rid):
        address_data = AddressData()
        return jsonify(address_data.getAllAddressesOfARegion(rid))

    def searchAddresses(self, args):
        address_id = args.get('address_id')
        user_id = args.get('user_id')
        region_id = args.get('region_id')

        if len(args) == 1 and address_id:
            if address_id:
                return self.getAddressById(int(address_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and user_id:
            if user_id:
                return self.getAddressOfUserByUserId(int(user_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and region_id:
            if region_id:
                return self.getAllAddressesOfARegion(int(region_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        else:
            return jsonify(Error="Malformed search string"), 400
