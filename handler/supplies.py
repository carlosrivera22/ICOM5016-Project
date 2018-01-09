from flask import jsonify
from dao.supplies import SuppliesData

class SuppliesHandler:

    def build_supplies_dict(self, row):
        result = {}
        result['supplies_id'] = row[0]
        result['supplier_id'] = row[1]
        result['resources_id'] = row[2]
        result['isFree'] = row[3]
        result['price'] = row[4]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['user_id'] = row[1]
        result['address_id'] = row[2]
        result['company_name'] = row[3]
        return result

    def getAllSupplies(self):
        supplies_dao = SuppliesData()
        supplies_list = supplies_dao.getAllSupplies()
        result_list = []
        for row in supplies_list:
            result = self.build_supplies_dict(row)
            result_list.append(result)
        return jsonify(Supplies = supplies_list)

    def getSuppliesBySupplierId(self, supplier_id):
        supplies_dao = SuppliesData()
        supplies_list = supplies_dao.getSuppliesBySupplierId(supplier_id)
        result_list = []
        for row in supplies_list:
            result = self.build_supplies_dict(row)
            result_list.append(result)
        return jsonify(Supplies = supplies_list)

    def getSuppliesByResourceId(self, resource_id):
        supplies_dao = SuppliesData()
        supplies_list = supplies_dao.getSuppliesByResourceId(resource_id)
        result_list = []
        for row in supplies_list:
            result = self.build_supplies_dict(row)
            result_list.append(result)
        return jsonify(Supplies = supplies_list)

    def getFreeSupplies(self):
        supplies_dao = SuppliesData()
        supplies_list = supplies_dao.getFreeSupplies()
        result_list = []
        for row in supplies_list:
            result = self.build_supplies_dict(row)
            result_list.append(result)
        return jsonify(Supplies = supplies_list)

    def getNonFreeSupplies(self):
        supplies_dao = SuppliesData()
        supplies_list = supplies_dao.getNonFreeSupplies()
        result_list = []
        for row in supplies_list:
            result = self.build_supplies_dict(row)
            result_list.append(result)
        return jsonify(Supplies = supplies_list)

    def searchSupplies(self, args):
        supplies_id = args.get('supplies_id')
        supplier_id = args.get('supplier_id')
        resource_id = args.get('resource_id')
        price = args.get('price')
        isFree = args.get('isFree')
        supplies_dao = SuppliesData()
        supplies_list = []

        if len(args) == 1 and supplier_id:
            supplies_list = supplies_dao.getSuppliesBySupplierId(supplier_id)
        elif len(args) == 1 and resource_id:
            supplies_list = supplies_dao.getSuppliesByResourceId(resource_id)
        elif len(args) == 1 and isFree:
            supplies_list = supplies_dao.getFreeSupplies()
        else:
            return jsonify(Error = "Malformed search string"), 400

        result_list = []

        for row in supplies_list:
            result = self.build_supplies_dict(row)
            result_list.append(result)

        return jsonify(Supplies = result_list)
