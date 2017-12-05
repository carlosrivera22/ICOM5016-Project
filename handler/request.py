from flask import jsonify
from data.request import RequestData

class RequestHandler:

    def getAllRequests(self):
        request_data = RequestData()
        return jsonify(request_data.getAllRequests())

    def getRequestById(self,rid):
        request_data = RequestData()
        return jsonify(request_data.getRequestById(rid))

    def getRequestsByVictimId(self,vid):
        request_data = RequestData()
        return jsonify(request_data.getRequestsByVictimId(vid))

    def getRequestsByResource(self,resid):
        request_data = RequestData()
        return jsonify(request_data.getRequestsByResource(resid))

    def searchRequests(self, args):
        request_id = args.get('request_id')
        status = args.get('status')
        date_submitted = args.get('date_submitted')
        resource_id = args.get('resource_id')
        victim_id = args.get('victim_id')

        if len(args) == 1 and request_id:
            if request_id:
                return self.getRequestById(int(request_id))
            else:
                return jsonify(Error="Malformed search string"), 400
        elif len(args) == 1 and victim_id:
            if victim_id:
                return self.getRequestsByVictimId(int(victim_id))
            else:
                return jsonify(Error="Malformed search string"), 400
        elif len(args) == 1 and resource_id:
            if resource_id:
                return self.getRequestsByResource(int(resource_id))
            else:
                return jsonify(Error="Malformed search string"), 400
        else:
            return jsonify(Error="Malformed search string"), 400
