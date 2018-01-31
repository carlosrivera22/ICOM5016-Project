from flask import jsonify
from dao.request_completed import RequestCompletedData

class RequestCompletedHandler:

    def build_sale_request_completed_dict(self,row):
        result={}
        result['request_id'] = row[0]
        result['date_resolved'] = row[1]
        result['order_type'] = row[2]
        result['supplier_id'] = row[3]
        result['victim_id'] = row[4]
        return result

    def build_transaction_dict(self,row):
        result = {}
        result['request_completed_id'] = [0]
        result['resource_name'] = row[1]
        result['date_resolved'] = row[2]
        result['price'] = row[3]
        result['company_name'] = row[4]
        result['victim_id'] = row[5]
        return result

    def build_request_completed_dict(self,row):
        result = {}
        result['resource_name'] = row[0]
        result['date_resolved'] = row[1]
        result['price'] = row[2]
        result['order_type'] = row[3]
        return result

    def build_request_completed_by_victim_id(self, row):
        result = {}
        result['request_completed_id'] = row[0]
        result['resource_name'] = row[1]
        result['price'] = row[2]
        result['quantity'] = row[3]
        result['total'] = row[4]
        result['date_resolved'] = row[5]
        result['order_type'] = row[6]
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

    def getAllSales(self):
        sale_data = RequestCompletedData()
        sale_list = sale_data.getAllSales()
        result_list = []
        for row in sale_list:
            result = self.build_sale_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Sales=result_list)

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
            result = self.build_request_completed_by_victim_id(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestCompletedByResourceId(self, resource_id):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getRequestCompletedByResourceId(resource_id)
        result_list = []
        for row in requests_completed_list:
            result = self.build_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

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


    def getSaleRequestCompletedByResourceId(self, resource_id):
        requests_completed_dao = RequestCompletedData()
        requests_completed_list = requests_completed_dao.getTransactionSaleRequestCompletedByResourceId(resource_id)
        result_list = []
        for row in requests_completed_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transaction=result_list)
#Mikael insert donation method.....................................................................................................
    def insertSale(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            date_resolved = form['date_resolved']
            supplier_id = form['supplier_id']
            victim_id = form['victim_id']
            resource_id = form['resource_id']
            quantity = int(form['quantity'])

            if date_resolved and supplier_id and victim_id and resource_id and quantity:
                dao = RequestCompletedData()
                request_completed_id = dao.insertSale(date_resolved, supplier_id, victim_id, resource_id, quantity)
                result = self.build_sale_attributes(request_completed_id, date_resolved, supplier_id, victim_id, resource_id, price, quantity)
                return jsonify(Sale=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
        
    def getAllSales(self):
        sale_data = RequestCompletedData()
        sale_list = sale_data.getAllSales()
        result_list = []
        for row in sale_list:
            result = self.build_sale_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Sales=result_list)

        
    def build_sale_attributes(self, request_completed_id, date_resolved, supplier_id, victim_id, resource_id, total, quantity):
        result = {}
        result['request_completed_id'] = request_completed_id
        result['date_resolved'] = date_resolved
        result['supplier_id'] = supplier_id
        result['victim_id'] = victim_id
        result['resource_id'] = resource_id
        result['total'] = total
        result['quantity'] = quantity
        return result
    
    def build_sale_request_completed_dict(self, row):
        result = {}
        result['request_completed_id'] = row[0]
        result['request_id'] = row[1]
        result['date_resolved'] = row[2]
        result['order_type'] = row[3]
        result['supplier_id'] = row[4]
        result['victim'] = row[5]
        result['resource_id'] = row[6]
        result['total'] = row[7]
        result['quantity'] = row[8]
        result['credit_card_id'] = row[9]
        result['credit_card_number'] = row[10]
        result['name_on_card'] = row[11]
        result['exp_date'] = row[12]
        result['cvs'] = row[13]
        return result
#............................................END OF SALES METHODS...................................................................................



#Mikael insert donation method.....................................................................................................
    def insertDonation(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            date_resolved = form['date_resolved']
            supplier_id = form['supplier_id']
            victim_id = form['victim_id']
            resource_id = form['resource_id']
            quantity = int(form['quantity'])

            if date_resolved and supplier_id and victim_id and resource_id and quantity:
                dao = RequestCompletedData()
                request_completed_id = dao.insertDonation(date_resolved, supplier_id, victim_id, resource_id, str(quantity))
                result = self.build_donation_attributes(request_completed_id, date_resolved, 'Donation', supplier_id, victim_id, resource_id, quantity)
                return jsonify(Donation=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllDonation(self):
        donation_data = RequestCompletedData()
        donation_list = donation_data.getAllDonation()
        result_list = []
        for row in donation_list:
            result = self.build_donation_request_completed_dict(row)
            result_list.append(result)
        return jsonify(Donation=result_list)

    def build_donation_attributes(self, request_completed_id, date_resolved, order_type, supplier_id, victim_id, resource_id, quantity):
        result = {}
        result['request_completed_id'] = request_completed_id
        result['date_resolved'] = date_resolved
        result['order_type'] = order_type
        result['supplier_id'] = supplier_id
        result['victim_id'] = victim_id
        result['resource_id'] = resource_id
        result['quantity'] = quantity
        return result
    
    def build_donation_request_completed_dict(self, row):
        result = {}
        result['request_completed_id'] = row[0]
        result['request_id'] = row[1]
        result['date_resolved'] = row[2]
        result['order_type'] = row[3]
        result['supplier_id'] = row[4]
        result['victim'] = row[5]
        result['resource_id'] = row[6]
        result['total'] = row[7]
        result['quantity'] = row[8]
        return result
#............................................END OF DONATIONS METHODS...................................................................................



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
