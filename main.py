from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler
from handler.region import RegionHandler
from handler.user import UserHandler
from handler.address import AddressHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Backend System for Disaster Site Resources Locator'

@app.route('/DisasterApp/suppliers',methods=["GET"])
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)

@app.route('/DisasterApp/regions')
def getAllRegions():
    if not request.args:
        return RegionHandler().getAllRegions()
    else:
        return RegionHandler().searchRegion(request.args)

@app.route('/DisasterApp/users')
def getAllUsers():
    if not request.args:
        return UserHandler().getAllUsers()
    else:
        return UserHandler().searchUsers(request.args)

@app.route('/DisasterApp/users/<int:user_id>')
def getUserById(user_id):
    return UserHandler().getUserById(user_id)

@app.route('/DisasterApp/addresses')
def getAllAdresses():
    if not request.args:
        return AddressHandler().getAllAdresses()
    else:
        return AddressHandler().searchAddresses(request.args)

@app.route('/DisasterApp/users/<int:user_id>/address')
def getAddressOfUserByUserId(user_id):
    return AddressHandler().getAddressOfUserByUserId(user_id)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
