class RequestCompletedData:

    request_completed = [

        {
            'request_completed_id': 1,
            'date_resolved': '12/01/2017',
            'order_type': 'Donation',
            'supplier_id': 3,
            'victim_id': 1,
            'resource_id': 4,
            'category_id': 2,
            'price': 0
        },

        {
            'request_completed_id': 2,
            'date_resolved': '18/09/2017',
            'order_type': 'Purchase',
            'supplier_id': 1,
            'victim_id': 2,
            'resource_id': 3,
            'category_id': 1,
            'price': 345.52
        },

        {
            'request_completed_id': 3,
            'date_resolved': '18/09/2017',
            'order_type': 'Donation',
            'supplier_id': 1,
            'victim_id': 3,
            'resource_id': 1,
            'category_id': 4,
            'price': 0
        },

        {
            'request_completed_id': 4,
            'date_resolved': '24/11/2017',
            'order_type': 'Purchase',
            'supplier_id': 2,
            'victim_id': 1,
            'resource_id': 4,
            'category_id': 2,
            'price': 50.00
        },

    ]

    def getAllRequestsCompleted(self):
        return self.request_completed

    def getRequestCompletedByID(self, request_completed_id):
        for r in self.request_completed:
            if r['request_completed_id'] == request_completed_id:
                return r
        return 'No Request Completed Found'

    def getRequestCompletedByDateResolved(self, date_resolved):
        results = []
        for r in self.request_completed:
            if r['date_resolved'] == date_resolved:
                results.append(r)
        return results

    def getRequestCompletedByOrderType(self, order_type):
        results = []
        for r in self.request_completed:
            if r['order_type'] == order_type:
                results.append(r)
        return results

    def getRequestCompletedBySupplierId(self, supplier_id):
        results = []
        for r in self.request_completed:
            if r['supplier_id'] == supplier_id:
                results.append(r)
        return results

    def getRequestCompletedByVictimId(self, victim_id):
        results = []
        for r in self.request_completed:
            if r['victim_id'] == victim_id:
                results.append(r)
        return results

    def getRequestCompletedByResourceId(self, resource_id):
        results = []
        for r in self.request_completed:
            if r['resource_id'] == resource_id:
                results.append(r)
        return results

    def getRequestCompletedByCategoryId(self, category_id):
        results = []
        for r in self.request_completed:
            if r['category_id'] == category_id:
                results.append(r)
        return results

    def getRequestCompletedByPrice(self, price):
        results = []
        for r in self.request_completed:
            if r['price'] == price:
                results.append(r)
        return results




