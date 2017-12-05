class RequestData:
    requests = [
        {
            'request_id':1,
            'status':'',
            'date_submitted':'',
            'resource_id':1,
            'victim_id':1
        },
        {
            'request_id':2,
            'status':'',
            'date_submitted':'',
            'resource_id':2,
            'victim_id':1
        },
        {
            'request_id':3,
            'status':'',
            'date_submitted':'',
            'resource_id':2,
            'victim_id':1
        }
    ]

    def getAllRequests(self):
        return self.requests

    def getRequestById(self,rid):
        for r in self.requests:
            if r['request_id'] == rid:
                return r
        return 'No request found'

    def getRequestsByVictimId(self,vid):
        for r in self.request:
            if r['victim_id'] == vid:
                return r
        return 'No request found'

    def getRequestsByResource(self,resid):
        for r in self.request:
            if r['resource_id'] == resid:
                return r
        return 'No request found'
