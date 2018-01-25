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

@app.route('/DisasterApp/allResources')
def getAllResources():
    return ResourceHandler().getAllResources()

# Available Resources route
@app.route('/DisasterApp/AvailableResources')
def getAvailableResources():
    return ResourceHandler().getAvailableResources()

@app.route('/DisasterApp/FreeResources')
def getFreeResources():
    return ResourceHandler().getFreeResources()

# Needed Resources route
@app.route('/DisasterApp/RequestedResources')
def getNeededResources():
    return RequestHandler().getAllRequestedResources()


# Supplier's products route
@app.route('/DisasterApp/supplier/<int:sid>/supplies')
def getResourcesBySupplierId(sid):
    return SupplierHandler().getResourcesBySupplierId(sid)


# Products supplied by Supplier route
@app.route('/DisasterApp/supplies/<string:rame>/supplier')
def getSuppliersByResource(rame):
    return SupplierHandler().getSuppliersByResource(rame)

# Products supplied by region route
@app.route('/DisasterApp/region/<int:region_id>/<int:resource_id>/resource')
def getResourceByRegionIdAndResourceId(region_id,resource_id):
    return DistributionRegionHandler().getResourcesByRegionIdAndResourceId(region_id,resource_id)

#=====================================================

# Request completed by Supplier route
@app.route('/DisasterApp/supplier/<int:sid>/requestsCompleted')
def getRequestCompletedBySupplierId(sid):
    return RequestCompletedHandler().getRequestCompletedBySupplierId(sid)


# Orders made by Victim
@app.route('/DisasterApp/victim/<int:victim_id>/requests')
def getRequestsByVictimId(victim_id):
    return DisasterVictimHandler().getRequestsByVictimId(victim_id)


# Keyword search resources being requested, with sorting by resource name
@app.route('/DisasterApp/resources/requested/<string:keyword>')
def getRequestedResourcesByKeyword(keyword):
    return RequestHandler().getAllRequestedResourcesByKeyword(keyword)


# Keyword search resources available, with sorting by resource name
@app.route('/DisasterApp/resources/available/<string:keyword>')
def getAvailableResourcesByKeyword(keyword):
    return ResourceHandler().getResourcesByKeywordAndAvailability(keyword,False,True)


# Get all credit cards
@app.route('/DisasterApp/CreditCards', methods=['GET','POST'])
def getAllCreditCards():
    if request.method == 'POST':
        return CreditCardHandler().insertCreditCard(request.form)
    else:
        if not request.args:
            return CreditCardHandler().getAllCreditCards()


#funciona phase3
@app.route('/DisasterApp/DisasterVictim', methods=['GET', 'POST'])
def getAllVictims():
    if request.method == 'POST':
        return DisasterVictimHandler().insertVictim(request.form)
    else:
        if not request.args:
            return DisasterVictimHandler().getAllDisasterVictims()
        else:
            return DisasterVictimHandler().searchVictims(request.args)

#funciona phase3
@app.route('/DisasterApp/Supplier', methods=['GET', 'POST'])
def getAllSupplier():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)


#funciona phase3
@app.route('/DisasterApp/Resource', methods=['GET', 'POST'])
def getAllResource():
    if request.method == 'POST':
        return ResourceHandler().insertResource(request.form)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)


# Not tested
@app.route('/Disaster/Resource/<int:resource_id>', methods=['GET','PUT'])
def getResourceByResourceId(resource_id):
    if request.method == 'GET':
        return ResourceHandler().getResourcesById(resource_id)
    elif request.method == 'PUT':
        return ResourceHandler().updateResource(resource_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


# Not tested
@app.route('/DisasterApp/Request', methods=['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        return RequestHandler().insertRequest(json.loads(list(request.form.to_dict().keys())[0]))
    else:
        if not request.args:
            return RequestHandler().getAllRequests()
        else:
            return RequestHandler().searchRequests(request.args)





if __name__ == '__main__':
    app.run(debug=True, port=8080)
