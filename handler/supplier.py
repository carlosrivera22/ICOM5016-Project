from flask import jsonify
from data.supplier import SupplierData

class SupplierHandler:
    def build_supplier_dict(self,row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['scity'] = row[2]
        result['sphone'] = row[3]
        return result

    def getAllSuppliers(self):
        #Phase 1: Devolvera hardcoded data
        supplier = SupplierData()
        return jsonify(supplier.getAllSuppliers())


    def getSupplierById(self,id):
        supplier = SupplierData()
        return jsonify(supplier.getSupplierById(id))