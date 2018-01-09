from flask import jsonify
from dao.supplier import SupplierDAO
from dao.resource import ResourceData

class SupplierHandler:

    def build_supplier_by_product_dict(self,row):
        result = {}
        result['first_name'] = row[0]
        result['last_name'] = row[1]
        result['company_name'] = row[2]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['company_name'] = row[5]
        result['street'] = row[6]
        result['city'] = row[7]
        result['state'] = row[8]
        result['country'] = row[9]
        result['zipcode'] = row[10]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['category_id'] = row[1]
        result['resource_name'] = row[2]
        result['isavailable'] = row[3]
        result['isneeded'] = row[4]
        result['quantity'] = row[5]
        result['keyword'] = row[6]
        return result

    def build_request_complete_dict(self, row):
        result = {}
        result['request_completed_id'] = row[0]
        result['request_id'] = row[1]
        result['date_resolved'] = row[2]
        result['order_type'] = row[3]
        result['supplier_id'] = row[4]
        result['victim_id']= row[5]
        result['resource_id'] = row[6]
        result['price'] = row[7]

    def build_supplier_attributes(self, supplier_id, user_id, address_id, company_name):
        result = {}
        result['supplier_id'] = supplier_id
        result['user_id'] = user_id
        result['address_id'] = address_id
        result['company_name'] = company_name
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSupplier()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, supplier_id):
        dao = SupplierDAO()
        row = dao.getSupplierById(supplier_id)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier =supplier)

    def getResourcesBySupplierId(self, supplier_id):
        dao = SupplierDAO()
        if not dao.getSupplierById(supplier_id):
            return jsonify(Error="Supplier Not Found"),404
        suppliers_list = dao.getResourcesBySupplierId(supplier_id)
        result_list = []
        for row in suppliers_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def searchSuppliers(self, args):
        first_name = args.get("first_name")
        last_name = args.get("last_name")
        email = args.get("email")
        phone = args.get("phone")
        company_name = args.get("company_name")
        dao = SupplierDAO()
        supplier_list = []

        if (len(args) == 1) and first_name:
            supplier_list = dao.getSupplierByFirstName(first_name)
        elif (len(args) == 1) and last_name:
            supplier_list = dao.getSupplierByLastName(last_name)
        elif (len(args) == 1) and email:
            supplier_list = dao.getSupplierByEmail(email)
        elif (len(args) == 1) and last_name:
            supplier_list = dao.getSupplierByPhone(phone)
        elif (len(args) == 1) and company_name:
            supplier_list = dao.getSupplierByLastName(company_name)
        else:
            return jsonify(Error = "Malformed query string"), 400

        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getResourcesBySupplierId(self, supplier_id):
        dao = SupplierDAO()
        if not dao.getSupplierById(supplier_id):
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getResourcesBySupplierId(supplier_id)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getRequestCompleteBySupplierId(self, supplier_id):
        dao = SupplierDAO()
        if not dao.getSupplierById(supplier_id):
            return jsonify(Error="Supplier Not Found"), 404
        request_completed_list = dao.getRequestedCompletedBySupplierId(supplier_id)
        result_list = []
        for row in request_completed_list:
            result = self.build_request_complete_dict(row)
            result_list.append(result)
        return jsonify(Request_Completed=result_list)

    def getSuppliersByResource(self, resource_name):
        dao = SupplierDAO()
        supplier_list = dao.getSuppliersByResource(resource_name)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_by_product_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)
