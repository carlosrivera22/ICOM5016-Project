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

    def build_annoucement_dit(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['resource_name'] = row[1]
        result['quantity'] = row[2]
        result['price'] = row[3]
        result['isavailable'] = row[4]
        result['first_name'] = row[5]
        result['last_name'] = row[6]
        result['company_name'] = row[7]
        return result


    def build_resource_attribute_dict(self, resource_id,category_id, resource_name, is_available, is_needed, quantity, keyword,
                                  subcategory_id, supplier_id, price, is_free):
        result = {}
        result['resource_id'] = resource_id
        result['category_id'] = category_id
        result['resource_name'] = resource_name
        result['is_available'] = is_available
        result['is_needed'] = is_needed
        result['quantity'] = quantity
        result['keyword'] = keyword
        result['subcategory_id'] = subcategory_id
        result['supplier_id'] = supplier_id
        result['price'] = price
        result['isfree'] = is_free
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
        row = resource_dao.getResourcesById(resource_id)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resources = resource)

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
            result = self.build_resource_dict(row)
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

    #get free resources PHASE3
    def getFreeResources(self):
        resource_dao = ResourceData()
        resource_list = resource_dao.getFreeResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return result

    def insertResource(self, form):
        if form and len(form) == 7:
            category_id = form['category_id']
            resource_name = form['resource_name']
            quantity = int(form['quantity'])
            keyword = form['keyword']
            subcategory_id = form['subcategory_id']
            supplier_id = form['supplier_id']
            price = float(form['price'])

            if category_id and resource_name and quantity and keyword and subcategory_id and supplier_id and price:
                dao = ResourceData()
                resource_id = dao.insert(category_id, resource_name, quantity, keyword, subcategory_id, supplier_id, price)
                result = {}
                result["category_id"] = category_id
                result["resource_name"] = resource_name
                result["quantity"] = quantity
                result["keyword"] = keyword
                result["subcategory_id"] = subcategory_id
                result["supplier_id"] = supplier_id
                result["price"] = price

                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request2")


    def updateResource(self, resource_id, form):
        dao = ResourceData()
        if not dao.getResourcesById(resource_id):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) != 11:
                return jsonify(Error="Malformed update request"), 400
            else:
                category_id = form['category_id']
                resource_name = form['resource_name']
                isavailable = form['isavailable']
                isneeded = form['isneeded']
                quantity = form['quantity']
                keyword = form['keyword']
                subcategory_id = form['subcategory_id']
                supplier_id = form['supplier_id']
                price = form['price']
                isfree = form['isfree']
                if category_id and resource_name and isavailable and isneeded and quantity and keyword and subcategory_id and supplier_id and price and isfree:
                    dao.update(resource_id, category_id, resource_name, isavailable, isneeded, quantity, keyword,
                               subcategory_id, supplier_id, price, isfree)
                    result = self.build_resource_attribute_dict(resource_id, category_id, resource_name, isavailable, isneeded,
                                                        quantity, keyword, subcategory_id, supplier_id, price, isfree)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def getAnnouncement(self):
        resource_dao = ResourceData()
        resource_list = resource_dao.getResourceAnnouncement()
        result_list = []
        for row in resource_list:
            result = self.build_annoucement_dit(row)
            result_list.append(result)
        return jsonify(Announcement=result_list)

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
