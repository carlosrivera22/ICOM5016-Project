import os
from flask import Flask, jsonify, request, render_template

from handler.resource import ResourceHandler
from handler.request import RequestHandler
from handler.supplier import SupplierHandler
from handler.request_completed import RequestCompletedHandler
from handler.disaster_victim import DisasterVictimHandler
from handler.distribution_region import DistributionRegionHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('index.html')

# Available Resources route
@app.route('/DisasterApp/AvailableResources')
def getAvailableResources():
    return ResourceHandler().getAvailableResources()


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


if __name__ == '__main__':
    #app.run(debug=True, port=8080)
    port = int(os.environ.get("PORT", 5432))
    app.run(debug=True, host="0.0.0.0", port=port)
