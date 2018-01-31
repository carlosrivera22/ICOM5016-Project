from flask import Flask, jsonify, request, render_template

from handler.resource import ResourceHandler
from handler.request import RequestHandler
from handler.supplier import SupplierHandler
from handler.request_completed import RequestCompletedHandler
from handler.disaster_victim import DisasterVictimHandler
from handler.distribution_region import DistributionRegionHandler
from handler.credit_card import CreditCardHandler
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def greeting():
    return render_template('index.html')

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# DISASTER VICTIM ROUTES

@app.route('/DisasterApp/DisasterVictim', methods=['GET', 'POST'])
def getAllVictims():
    if request.method == 'POST':
        return DisasterVictimHandler().insertVictim(request.form.to_dict())
    else:
        if not request.args:
            return DisasterVictimHandler().getAllDisasterVictimsInfo()
        else:
            return DisasterVictimHandler().searchVictims(request.args)

@app.route('/DisasterApp/DisasterVictim/<int:victim_id>', methods=['GET'])
def getVictimInfoById(victim_id):
    if request.method == 'GET':
        return DisasterVictimHandler().getVictimInfoById(victim_id)
    else:
        return DisasterVictimHandler().searchVictims(request.args)

#9.a
@app.route('/DisasterApp/DisasterVictim/<int:victim_id>/Request')
def getRequestsByVictimId(victim_id):
    return RequestHandler().getRequestsInfoByVictimId(victim_id)

#9.b
@app.route('/DisasterApp/DisasterVictim/<int:victim_id>/RequestCompleted')
def getRequestCompletedByVictimId(victim_id):
    return RequestCompletedHandler().getRequestCompletedByVictimId(victim_id)

@app.route('/DisasterApp/DisasterVictim/<int:victim_id>/CreditCards')
def getVictimCreditCard(victim_id):
    return DisasterVictimHandler().getVictimCreditCard(victim_id)

# ------------------------------------------------------------------------------

# SUPPLIER ROUTES

@app.route('/DisasterApp/Supplier', methods=['GET', 'POST'])
def getAllSupplier():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form.to_dict())
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)

@app.route('/DisasterApp/Supplier/<int:supplier_id>', methods=['GET'])
def getSupplierById(supplier_id):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(supplier_id)
    else:
        return SupplierHandler().searchSuppliers(request.args)

#6
@app.route('/DisasterApp/Supplier/<int:supplier_id>/Resources')
def getResourcesBySupplierId(supplier_id):
    return SupplierHandler().getResourcesBySupplierId(supplier_id)

#10
@app.route('/DisasterApp/Supplier/<int:supplier_id>/RequestCompleted')
def getRequestCompletedBySupplierId(sid):
    return RequestCompletedHandler().getRequestCompletedBySupplierId(supplier_id)

# ------------------------------------------------------------------

# RESOURCE ROUTES

@app.route('/DisasterApp/Resource', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourceHandler().insertResource(request.form.to_dict())
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)

#
@app.route('/DisasterApp/Resource/<int:resource_id>', methods=['GET', 'PUT'])
def getResourcesByResourceId(resource_id):
    if request.method == 'GET':
        return ResourceHandler().getResourcesById(resource_id)
    elif request.method == 'PUT':
        return ResourceHandler().updateResource(resource_id, request.form.to_dict())
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DisasterApp/Resource/Free')
def getFreeResources():
    return ResourceHandler().getFreeResources()

#2
@app.route('/DisasterApp/Resource/Available')
def getAvailableResources():
    return ResourceHandler().getAvailableResources()

#5
@app.route('/DisasterApp/Resource/Available/<string:keyword>')
def getAvailableResourcesByKeyword(keyword):
    return ResourceHandler().getResourcesByKeywordAndAvailability(keyword,False,True)

#3
@app.route('/DisasterApp/Resource/Request')
def getNeededResources():
    return RequestHandler().getAllRequestedResources()

#4
@app.route('/DisasterApp/Resource/Request/<string:keyword>')
def getRequestedResourcesByKeyword(keyword):
    return RequestHandler().getAllRequestedResourcesByKeyword(keyword)

#7
@app.route('/DisasterApp/Resource/<string:resource_id>/Supplier')
def getSuppliersByResource(rame):
    return SupplierHandler().getSuppliersOfResourceId(resource_id)

#8
@app.route('/DisasterApp/Resource/<int:resource_id>/Region/<int:region_id>')
def getResourceByRegionIdAndResourceId(region_id, resource_id):
    return DistributionRegionHandler().getResourcesByRegionIdAndResourceId(region_id, resource_id)

# ------------------------------------------------------------------------------

@app.route('/DisasterApp/DisasterVictim/CreditCard', methods=['GET','POST'])
def getAllCreditCards():
    if request.method == 'POST':
        return CreditCardHandler().insertCreditCard(json.loads(request.form.to_dict())
    else:
        if not request.args:
            return CreditCardHandler().getAllCreditCards()

# works phase3
@app.route('/DisasterApp/DisasterVictim/Request', methods=['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.form.to_dict())
    else:
        if not request.args:
            return RequestHandler().getAllRequests()
        else:
            return RequestHandler().searchRequests(request.args)

#Credit Card Update - funciona phase3
@app.route('/DisasterApp/CreditCard/<int:credit_card_id>', methods=['GET','PUT'])
def getCreditCardById(credit_card_id):
    if request.method == 'GET':
        return CreditCardHandler().getCreditCardById(credit_card_id)
    elif request.method == 'PUT':
        return CreditCardHandler().updateCreditCard(credit_card_id, request.form.to_dict())
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Transaction of a Resource - funciona
@app.route('/DisasterApp/Request_Completed/<int:resource_id>', methods=['GET'])
def getRequestCompletedByResourceId(resource_id):
    if request.method == 'GET':
        return RequestCompletedHandler().getSaleRequestCompletedByResourceId(resource_id)
    else:
        return jsonify(Error="Method not allowed."), 405

# NOT TESTED
@app.route('/DisasterApp/RequestCompleted/Sale/', methods=['GET', 'POST'])
def getAllSaleRequestCompleted():
    if request.method == 'POST':
        return RequestCompletedHandler().insertSale(request.form.to_dict())
    else:
        if not request.args:
            return RequestCompletedHandler().getAllSales()

@app.route('/DisasterApp/Resource/Announcement', methods=['GET'])
def getResourceAnnouncement():
    if request.method == 'GET':
        return ResourceHandler().getAnnouncement()
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/RequestCompleted/Donation/', methods=['GET', 'POST'])
def getAllDonationRequestCompleted():
    if request.method == 'POST':
        return RequestCompletedHandler().insertDonation(request.form.to_dict())
    else:
        if not request.args:
            return RequestCompletedHandler().getAllDonation()

if __name__ == '__main__':
    app.run(debug=True, port=5000)