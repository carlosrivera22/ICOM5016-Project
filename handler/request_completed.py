from flask import jsonify
from data.request_completed import RequestCompletedData

class RequestCompletedHandler:

    def getAllRequestsCompleted(self):
        request_completed = RequestCompletedData()
        return jsonify(request_completed.getAllRequestsCompleted())

    def getRequestCompletedById(self, request_completed_id):
        request_completed = RequestCompletedData()
        result = request_completed.getRequestCompletedByID(request_completed_id)
        return jsonify(result)

    def getRequestCompletedByDateResolved(self, date_resolved):
        request_completed = RequestCompletedData()
        result = request_completed.getRequestCompletedByDateResolved(date_resolved)
        return jsonify(result)

    def getRequestCompletedByOrderType(self, order_type):
        request_completed = RequestCompletedData()
        result = request_completed.getRequestCompletedByOrderType(order_type)
        return jsonify(result)

    def getRequestCompletedBySupplierId(self, supplier_id):
        request_completed = RequestCompletedData()
        result = request_completed.getRequestCompletedBySupplierId(supplier_id)
        return jsonify(result)

    def getRequestCompletedByVictimId(self, victim_id):
        request_completed = RequestCompletedData()
        result = request_completed.getRequestCompletedByVictimId(victim_id)
        return jsonify(result)

    def getRequestCompletedByResourceId(self, resource_id):
        request_completed = RequestCompletedData()
        result = request_completed.getRequestCompletedByResourceId(resource_id)
        return jsonify(result)

    def getRequestCompletedByCategoryId(self, category_id):
        request_completed = RequestCompletedData()
        result = request_completed.getRequestCompletedByCategoryId(category_id)
        return jsonify(result)

    def getRequestCompletedByPrice(self, price):
        request_completed = RequestCompletedData()
        result = request_completed.getRequestCompletedByPrice(price)
        return jsonify(result)

    def searchRequestCompleted(self, args):
        request_completed_id = args.get['request_completed_id']
        date_resolved = args.get['date_resolved']
        order_type = args.get['order_type']
        supplier_id = args.get['supplier_id']
        victim_id = args.get['victim_id']
        resource_id = args.get['respurce_id']
        category_id = args.get['category_id']
        price = args.get['price']

        if len(args) == 1 and request_completed_id:
            if request_completed_id:
                return self.getRequestCompletedById(int(request_completed_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and date_resolved:
            if date_resolved:
                return self.getRequestCompletedByDateResolved(date_resolved)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and order_type:
            if order_type:
                return self.getRequestCompletedByOrderType(order_type)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and supplier_id:
            if supplier_id:
                return self.getRequestCompletedBySupplierId(int(supplier_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and victim_id:
            if victim_id:
                return self.getRequestCompletedByVictimId(int(victim_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and resource_id:
            if resource_id:
                return self.getRequestCompletedByResourceId(int(resource_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and category_id:
            if category_id:
                return self.getRequestCompletedByCategoryId(int(category_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and price:
            if price:
                return self.getRequestCompletedByPrice(int(price))
            else:
                return jsonify(Error="Malformed search string."), 400
        else:
            return jsonify(Error="Malformed search string"), 400





