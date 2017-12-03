from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler


app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Backend System for Disaster Site Resources Locator'

@app.route('/DisasterApp/suppliers',methods=["GET"])
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return "Here"


@app.route('/DisasterApp/suppliers/<int:sid>')
def getSupplierById(sid):
    supplier = SupplierHandler()
    return supplier.getSupplierById(sid)


@app.route('/DisasterApp/suppliers/')
def getSupplierById1():
    supplier = SupplierHandler()
    id = request.args.get('supplier_id','default supplier_id')
    id = int(id)
    return supplier.getSupplierById(id)


if __name__ == '__main__':
    app.run(debug=True, port=8080)