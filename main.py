from flask import Flask, jsonify, request, render_template

from handler.resource import ResourceHandler
from handler.request import RequestHandler
from handler.supplier import SupplierHandler
from handler.request_completed import RequestCompletedHandler
from handler.disaster_victim import DisasterVictimHandler
from handler.distribution_region import DistributionRegionHandler
from handler.credit_card import CreditCardHandler

app = Flask(__name__)



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



@app.route('/DisasterApp/DisasterVictim', methods=['GET', 'POST'])
def getAllVictims():
    if request.method == 'POST':
        return DisasterVictimHandler().insertVictim(request.form)
    else:
        if not request.args:
            return DisasterVictimHandler().getAllDisasterVictims()
        else:
            return DisasterVictimHandler().searchVictims(request.args)


@app.route('/DisasterApp/Supplier', methods=['GET', 'POST'])
def getAllSupplier():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)


result = {}
result["category_id"] = "1"
result["resource_name"] = "Great Value"
result["isavailable"] = "TRUE"
result["isneeded"] = "TRUE"
result["quantity"] = "12"
result["keyword"] = "Great Value"
result["subcategory_id"] = "1"
result["supplier_id"] = "3"
result["price"] = "5.00"
result["isfree"] = "FALSE"

@app.route('/DisasterApp/Resource', methods=['GET', 'POST'])
def getAllResource():
    #if request.method == 'POST':
        return ResourceHandler().insertResource(result)
    #else:
        #if not request.args:
           # return ResourceHandler().getAllResources()
        #else:
            #return ResourceHandler().searchResources(request.args)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
