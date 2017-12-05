from flask import Flask, jsonify, request

from handler.category import CategoryHandler
from handler.credit_card import CreditCardHandler
from handler.request_completed import RequestCompletedHandler
from handler.sub_category import SubCategoryHandler
from handler.supplier import SupplierHandler
from handler.region import RegionHandler
from handler.user import UserHandler
from handler.address import AddressHandler
from handler.bank_account import BankAccountHandler
from handler.disaster_victim import DisasterVictimHandler
from handler.request import RequestHandler
from handler.administrator import AdminHandler


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
def getAllAddresses():
    if not request.args:
        return AddressHandler().getAllAddresses()
    else:
        return AddressHandler().searchAddresses(request.args)

@app.route('/DisasterApp/users/<int:user_id>/address')
def getAddressOfUserByUserId(user_id):
    return AddressHandler().getAddressOfUserByUserId(user_id)

@app.route('/DisasterApp/bankAccounts')
def getAllBankAccounts():
    if not request.args:
        return BankAccountHandler().getAllBankAccount()
    else:
        return BankAccountHandler().searchBankAccount(request.args)

@app.route('/DisasterApp/bankAccounts/<int:supplier_id>/supplier')
def getBankAccountBySupplierId(supplier_id):
    return BankAccountHandler().getBankAccountBySupplierId(supplier_id)

@app.route('/DisasterApp/categories')
def getAllCategories():
    if not request.args:
        return CategoryHandler().getAllCategories()
    else:
        return CategoryHandler().searchCategory(request.args)

@app.route('/DisasterApp/categories/<int:category_id>')
def getCategoryById(category_id):
    return CategoryHandler().getCategoryById(category_id)

@app.route('/DisasterApp/categories/<string:category_name>')
def getCategoryByName(category_name):
    return CategoryHandler().getCategoryByName(category_name)

@app.route('/DisasterApp/subCategories')
def getAllSubCategories():
    if not request.args:
        return SubCategoryHandler().getAllSubCategories()
    else:
        return SubCategoryHandler().searchSubCategory(request.args)

@app.route('/DisasterApp/subCategories/<int:sub_category_id>')
def getSubCategoryById(sub_category_id):
    return SubCategoryHandler().getSubCategoryById(sub_category_id)

@app.route('/DisasterApp/subCategories/<string:sub_category_name>')
def getSubCategoryByName(sub_category_name):
    return SubCategoryHandler().getSubCategoryByName(sub_category_name)

@app.route('/DisasterApp/subCategories/<int:category_id>/category')
def getSubCategoryByCategoryId(category_id):
    return SubCategoryHandler().getSubCategoryByCategoryId(category_id)

@app.route('/DisasterApp/creditCards')
def getAllCreditCards():
    if not request.args:
        return CreditCardHandler().getAllCreditCards()
    else:
        return CreditCardHandler().searchCreditCart(request.args)

@app.route('/DisasterApp/creditCards/<int:credit_card_id>')
def getCreditCardById(credit_card_id):
    return CreditCardHandler().getCreditCardById(credit_card_id)

@app.route('/DisasterApp/creditCards/<string:name_on_card>')
def getCreditCardByNameOnCard(name_on_card):
    return CreditCardHandler().getCreditCardByNameOnCard(name_on_card)

@app.route('/DisasterApp/creditCards/<int:victim_id>/disasterVictim')
def getCreditCardByVictimId(victim_id):
    return CreditCardHandler().getCreditCardByVictimId(victim_id)

@app.route('/DisasterApp/requestsCompleted')
def getAllRequestsCompleted():
    if not request.args:
        return RequestCompletedHandler().getAllRequestsCompleted()
    else:
        return RequestCompletedHandler().searchRequestCompleted(request.args)

@app.route('/DisasterApp/requestsCompleted/<int:request_completed_id>')
def getrequestCompletedById(request_completed_id):
    return RequestCompletedHandler().getRequestCompletedById(request_completed_id)

#@app.route('/DisasterApp/requestsCompleted/<string:date_resolved>/dateResolved')
#def getrequestCompletedByDateResolved(date_resolved):
#    return RequestCompletedHandler().getRequestCompletedByDateResolved(date_resolved)

@app.route('/DisasterApp/requestsCompleted/<string:order_type>/orderType')
def getrequestCompletedByOrderType(order_type):
    return RequestCompletedHandler().getRequestCompletedByOrderType(order_type)

@app.route('/DisasterApp/requestsCompleted/<int:supplier_id>/supplier')
def getrequestCompletedBySupplierId(supplier_id):
    return RequestCompletedHandler().getRequestCompletedBySupplierId(supplier_id)

@app.route('/DisasterApp/requestsCompleted/<int:victim_id>/disasterVictim')
def getrequestCompletedByVictimId(victim_id):
    return RequestCompletedHandler().getRequestCompletedByVictimId(victim_id)

@app.route('/DisasterApp/requestsCompleted/<int:resource_id>/resource')
def getrequestCompletedByResourceId(resource_id):
    return RequestCompletedHandler().getRequestCompletedByResourceId(resource_id)

@app.route('/DisasterApp/requestsCompleted/<int:category_id>/category')
def getrequestCompletedByCategoryId(category_id):
    return RequestCompletedHandler().getRequestCompletedByCategoryId(category_id)

@app.route('/DisasterApp/requestsCompleted/<float:price>/price')
def getrequestCompletedByPrice(price):
    return RequestCompletedHandler().getRequestCompletedByPrice(price)

@app.route('/DisasterApp/DisasterVictims')
def getAllDisasterVictims():
    return DisasterVictimHandler().getAllDisasterVictims()

@app.route('/DisasterApp/victim/<int:victim_id>')
def getVictimById(victim_id):
    return DisasterVictimHandler().getVictimById(victim_id)




if __name__ == '__main__':
    app.run(debug=True, port=8080)
