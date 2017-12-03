from flask import jsonify
from data.supplier import SupplierData

class SupplierHandler:

    def getAllSuppliers(self):
        #Phase 1: Devolvera hardcoded data
        supplier = SupplierData()
        return jsonify(supplier.getAllSuppliers())

    def getSupplierById(self,id):
        supplier = SupplierData()
        result = supplier.getSupplierById(id)
        return jsonify(result)

    def getSuppliersByRegionId(self,region_id):
        supplier = SupplierData()
        result = supplier.getSuppliersByRegionId(region_id)
        return jsonify(result)

    def getSuppliersByAddressID(self,address_id):
        supplier = SupplierData()
        result = supplier.getSuppliersByAddressId(address_id)
        return jsonify(result)

    # WE CAN MAKE FUNCTIONS TO FIND DETAILS ABOUT THE ADDRESS OF THE SUPPLIER THROUGH THE address_id
    # FUNCTIONS CAN GO IN HERE....

    def getSuppliersByCompanyName(self,company_name):
        supplier = SupplierData()
        result = supplier.getSuppliersByCompanyName(company_name)
        return jsonify(result)

    def getSuppliersByRegionName(self,region_name):
        supplier = SupplierData()
        result = supplier.getSuppliersByRegion(region_name)
        return jsonify(result)

    def getSupplierByRegionIdAndCompanyName(self, region_id, company_name):
        supplier = SupplierData()
        result = supplier.getSupplierByRegionIdAndCompanyName(region_id,company_name)
        return jsonify(result)

    def getSupplierByRegionIdAndAdressId(self,region_id,address_id):
        supplier = SupplierData()
        result = supplier.getSupplierByRegionIdAndAddressId(region_id,address_id)
        return jsonify(result)

    def getSupplierByAddressIdAndCompanyName(self,address_id,company_name):
        supplier = SupplierData()
        result = supplier.getSupplierByAddressIdAndCompanyName(address_id,company_name)
        return jsonify(result)

    def searchSuppliers(self, args):
        region_name = args.get('region_name')
        company_name = args.get('company_name')
        region_id = args.get('region_id')
        address_id = args.get('address_id')
        if len(args) == 1 and region_name:
            if region_name:
                return self.getSuppliersByRegionName(region_name)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and company_name:
            if company_name:
                return self.getSuppliersByCompanyName(company_name)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and region_id:
            if region_id:
                return self.getSuppliersByRegionId(int(region_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and address_id:
            if address_id:
                return self.getSuppliersByAddressID(int(address_id))
            else:
                return jsonify(Error="Malformed search string"), 400
        elif len(args) == 2 and region_name and company_name:
            #create function that serves in a specific regionn to find a supplier with a company
            return("nothing")
        elif len(args) == 2 and region_id and company_name:
            return self.getSupplierByRegionIdAndCompanyName(int(region_id),company_name)
        elif len(args) == 2 and region_id and address_id:
            return self.getSupplierByRegionIdAndAdressId(int(region_id),int(address_id))
        elif len(args) == 2 and address_id and company_name:
            return self.getSupplierByAddressIdAndCompanyName(int(address_id),company_name)

        #more possible combinations can go here ----
        #...
        #...
        else:
            return jsonify(Error="Malformed search string"), 400







