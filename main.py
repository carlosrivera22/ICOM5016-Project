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

#11
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

#14
@app.route('/DisasterApp/DisasterVictim/Request', methods=['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.form.to_dict())
    else:
        if not request.args:
            return RequestHandler().getAllRequests()
        else:
            return RequestHandler().searchRequests(request.args)

#18
@app.route('/DisasterApp/DisasterVictim/CreditCard', methods=['GET','POST'])
def getAllCreditCards():
    if request.method == 'POST':
        return CreditCardHandler().insertCreditCard(request.form.to_dict())
    else:
        if not request.args:
            return CreditCardHandler().getAllCreditCards()

@app.route('/DisasterApp/DisasterVictim/<int:victim_id>/CreditCard')
def getVictimCreditCard(victim_id):
    return DisasterVictimHandler().getVictimCreditCard(victim_id)

#20
@app.route('/DisasterApp/DisasterVictim/CreditCard/<int:credit_card_id>', methods=['GET','PUT'])
def getCreditCardById(credit_card_id):
    if request.method == 'GET':
        return CreditCardHandler().getCreditCardById(credit_card_id)
    elif request.method == 'PUT':
        return CreditCardHandler().updateCreditCard(credit_card_id, request.form.to_dict())
    else:
        return jsonify(Error="Method not allowed."), 405

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
@app.route('/DisasterApp/Supplier/<int:supplier_id>/Resource')
def getResourcesBySupplierId(supplier_id):
    return SupplierHandler().getResourcesBySupplierId(supplier_id)

#10
@app.route('/DisasterApp/Supplier/<int:supplier_id>/RequestCompleted')
def getRequestCompletedBySupplierId(supplier_id):
    return RequestCompletedHandler().getRequestCompletedInfoBySupplierId(supplier_id)

# ------------------------------------------------------------------

# RESOURCE ROUTES

#12
@app.route('/DisasterApp/Resource', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourceHandler().insertResource(request.form.to_dict())
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)

#19
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
@app.route('/DisasterApp/Resource/<int:resource_id>/Supplier')
def getSuppliersByResource(resource_id):
    return SupplierHandler().getSuppliersOfResourceId(resource_id)

#8
@app.route('/DisasterApp/Resource/<int:resource_id>/Region/<int:region_id>')
def getResourceByRegionIdAndResourceId(region_id, resource_id):
    return DistributionRegionHandler().getResourcesByRegionIdAndResourceId(region_id, resource_id)

@app.route('/DisasterApp/Resource/Region/<int:region_id>')
def getResourceByRegionId(region_id):
    return ResourceHandler().getResourcesByRegionId(region_id)
# ------------------------------------------------------------------------------

# REQUESTS ROUTES

@app.route('/DisasterApp/RequestCompleted', methods=['GET'])
def getAllRequestsCompleted():
        return RequestCompletedHandler().getAllRequestsCompleted()

@app.route('/DisasterApp/Request/Completed/<int:request_completed_id>', methods=['GET'])
def getAllRequestsCompletedByRequestCompletedID(request_completed_id):
        return RequestCompletedHandler().getRequestCompletedById(request_completed_id)

@app.route('/DisasterApp/Request/<int:request_id>', methods=['GET'])
def getAllRequestByRequestID(request_id):
        return RequestHandler().getRequestById(request_id)

#17
@app.route('/DisasterApp/RequestCompleted/<int:resource_id>', methods=['GET'])
def getRequestCompletedByResourceId(resource_id):
    if request.method == 'GET':
        return RequestCompletedHandler().getSaleRequestCompletedByResourceId(resource_id)
    else:
        return jsonify(Error="Method not allowed."), 405

#15
@app.route('/DisasterApp/RequestCompleted/Sale', methods=['GET', 'POST'])
def getAllSaleRequestCompleted():
    if request.method == 'POST':
        return RequestCompletedHandler().insertSale(request.form.to_dict())
    else:
        if not request.args:
            return RequestCompletedHandler().getAllSales()

#16
@app.route('/DisasterApp/RequestCompleted/Donation', methods=['GET', 'POST'])
def getAllDonationRequestCompleted():
    if request.method == 'POST':
        return RequestCompletedHandler().insertDonation(request.form.to_dict())
    else:
        if not request.args:
            return RequestCompletedHandler().getAllDonation()


@app.route('/DisasterApp/Supplier/Region/<int:region_id>')
def getSuppliersByRegionId(region_id):
    return SupplierHandler().getSupplierByRegionId(region_id)


#Announcement Routes.....................................................................................................................................................
#1
#13
@app.route('/DisasterApp/Resource/Announcement', methods=['GET', 'POST'])
def getAllResourceAnnouncement():
    if request.method == 'POST':
        return ResourceHandler().insertAnnouncement(request.form.to_dict())
    else:
        return ResourceHandler().getAllAnnouncement()

@app.route('/DisasterApp/Resource/<int:resource_id>/Announcement/')
def getAnnouncementByResourceId(resource_id):
        return ResourceHandler().getAnnouncementByResourceId(resource_id)
#End of announcement routes.............................................................................................................................................

if __name__ == '__main__':
    app.run(debug=True, port=5000)