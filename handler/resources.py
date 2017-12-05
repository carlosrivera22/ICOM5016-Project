from flask import jsonify
from data.resource import ResourceData

class ResourceHandler:

    def getAllResources(self):
        resource_data = ResourceData()
        return jsonify(resource_data)

    def getResourceByNamw(self,resource_name):
        resource_data = ResourceData()
        return jsonify(resource_data.getResourcesByName(resource_name))

