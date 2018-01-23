from flask import jsonify
from dao.request_completed import RequestCompletedData

class RequestCompletedHandler:

    def build_request_completed_dict(self,row):
        result = {}
        result['resource_name'] = row[0]
        result['date_resolved'] = row[1]
        result['price'] = row[2]
        result['order_type'] = row[3]
        return result

    def build_request_dict(self, row):
        result = {}
        result['request_id'] = row[0]
        result['status'] = row[1]
        result['date_submitted'] = row[2]
        result['resource_id'] = row[3]
        return result


    def build_victim_dict(self, row):
        result = {}
        result['victim_id'] = row[0]
        result['user_id'] = row[1]
        result['address_id'] = row[2]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['category_id'] = row[1]
        result['resource_name'] = row[2]
        result['is_available'] = row[3]
        result['quantity'] = row[4]
        result['keyword'] = row[5]
        return result

    def getAllRequestsCompleted(self):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getAllRequestsCompleted()
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedById(self, request_completed_id):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedByID(request_completed_id)
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedByDateResolved(self, date_resolved):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedByDateResolved(date_resolved)
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedByOrderType(self, order_type):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedByOrderType(order_type)
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedBySupplierId(self, supplier_id):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedBySupplierId(supplier_id)
        result_list = []

        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedByVictimId(self, victim_id):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedByVictimId(victim_id)
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedByResourceId(self, resource_id):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedByResourceId(resource_id)
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedByCategoryId(self, category_id):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedByCategoryId(category_id)
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedByPrice(self, price):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedByPrice(price)
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)


    def searchRequestsCompleted(self, args):
        request_completed_id = args.get['request_completed_id']
        date_resolved = args.get['date_resolved']
        order_type = args.get['order_type']
        supplier_id = args.get['supplier_id']
        victim_id = args.get['victim_id']
        resource_id = args.get['respurce_id']
        category_id = args.get['category_id']
        price = args.get['price']

        if len(args) == 1 and request_completed_id:
            return self.getRequestCompletedById(int(request_completed_id))

        elif len(args) == 1 and date_resolved:
            return self.getRequestCompletedByDateResolved(date_resolved)

        elif len(args) == 1 and order_type:
            return self.getRequestCompletedByOrderType(order_type)

        elif len(args) == 1 and supplier_id:
            return self.getRequestCompletedBySupplierId(int(supplier_id))

        elif len(args) == 1 and victim_id:
            return self.getRequestCompletedByVictimId(int(victim_id))

        elif len(args) == 1 and resource_id:
            return self.getRequestCompletedByResourceId(int(resource_id))

        elif len(args) == 1 and category_id:
            return self.getRequestCompletedByCategoryId(int(category_id))

        elif len(args) == 1 and price:
            return self.getRequestCompletedByPrice(int(price))

        else:
            return jsonify(Error="Malformed search string"), 400
