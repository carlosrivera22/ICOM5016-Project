from flask import jsonify
from dao.resource import ResourceData

class ResourceHandler:

    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['category_id'] = row[1]
        result['resource_name'] = row[2]
        result['is_available'] = row[3]
        result['is_needed'] = row[4]
        result['quantity'] = row[5]
        result['keyword'] = row[6]
        return result

    def getAllResources(self):
        resource_dao = ResourceData()
        resource_list = resource_dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getResourcesById(self,resource_id):
        resource_dao = ResourceData()
        resource_list = resource_dao.getResourcesById(resource_id)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getAvailableResources(self):
        resource_dao = ResourceData()
        resource_list = resource_dao.getAvailableResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getNeededResources(self):
        resource_dao = ResourceData()
        resource_list = resource_dao.getNeededResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getResourcesByName(self,resource_name):
        resource_dao = ResourceData()
        row = resource_dao.getResourcesByName(resource_name)
        if not row:
            return jsonify(Error = "Resource not exist"), 404
        else:
            result = this.build_resource_dict(row)
        return jsonify(Resource = result)

    def getResourcesByKeyword(self, keyword):
        resource_dao = ResourceData()
        resource_list = resource_dao.getResourcesByKeyword(keyword)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getResourcesByKeywordAndAvailability(self, keyword, by_needed, by_available):
        resource_dao = ResourceData()
        resource_list = resource_dao.getResourcesByKeywordAndAvailability(keyword, by_needed, by_available)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)


    def searchResources(self, args):
        resource_id = args.get('victim_id')
        resource_name = args.get('user_id')
        is_available = args.get('address_id')
        is_needed = args.get('is_needed')
        quantity = args.get('quantity')
        keyword = args.get('keyword')
        resource_dao = ResourceData()
        resource_list = []

        if len(args) == 2 and resource_name and quantity:
            resource_list = resource_dao.getResourceQuantity(resource_name)
        else:
            return jsonify(Error = "Malformed Search String"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resource = result_list)
