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
        return "nothing"

    # WE CAN MAKE FUNCTIONS TO FIND DETAILS ABOUT THE ADDRESS OF THE SUPPLIER THROUGH THE address_id
    # FUNCTIONS CAN GO IN HERE....

    def getSuppliersByCompanyName(self,company_name):
        return "nothing"



    def searchSuppliers(self, args):
        region_name = args.get('region_name')
        company_name = args.get('company_name')
        region_id = args.get('region_id')
        address_id = args.get('address_id')
        if len(args) == 1 and region_name:
            if region_name:
                data = SupplierData()
                supplier_list = data.getSuppliersByRegion(region_name)
                return jsonify(supplier_list)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and company_name:
            if company_name:
                data = SupplierData()
                #needs finishing
                return jsonify("nothing")
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and region_id:
            if region_id:
                return self.getSuppliersByRegionId(int(region_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and address_id:
            if address_id:
                data = SupplierData()
                #needs finishing
                return jsonify('nothing')
            else:
                return jsonify(Error="Malformed search string"), 400
        elif len(args) == 2 and region_name and company_name:
            #create function that serves in a specific regionn to find a supplier with a company
            return("nothing")
        elif len(args) == 2 and region_id and company_name:
            # create function that serves in a specific region to find a supplier with a company
            return("nothing")
        elif len(args) == 2 and region_id and address_id:
            #create a function to find a region that
            return("nothing")
        #more possible combinations can go here ----
        #...
        #...
        else:
            return jsonify(Error="Malformed search string"), 400







