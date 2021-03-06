from flask import jsonify
from dao.request import RequestData

class RequestHandler:

    def build_request_dict(self, row):
        result = {}
        result['request_id'] = row[0]
        result['date_submited'] = row[1]
        result['resource_id'] = row[2]
        return result

    def build_request_info_dict(self, row):
        result = {}
        result['victim_id'] = row[0]
        result['resouce_name'] = row[1]
        result['date_submited'] = row[2]
        result['is_available'] = row[3]
        result['quantity'] = row[4]
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

    def build_requested_resources_dict(self,row):
        result = {}
        result['resource_name'] = row[0]
        return result

    def getAllRequests(self):
        requests_dao = RequestData()
        requests_list = requests_dao.getAllRequests()
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getAllRequestedResources(self):
        requests_dao = RequestData()
        requests_list = requests_dao.getAllRequestedResources()
        result_list = []
        for row in requests_list:
            result = self.build_requested_resources_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getAllRequestedResourcesByKeyword(self,keyword):
        requests_dao = RequestData()
        requests_list = requests_dao.getAllRequestedResourcesByKeyword(keyword)
        result_list = []
        for row in requests_list:
            result = self.build_requested_resources_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestById(self,rid):
        requests_dao = RequestData()
        row = requests_dao.getRequestById(rid)
        if not row:
            return jsonify(Error = "Request Not Found"), 404
        else:
            result = self.build_request_dict(row)
        return jsonify(Request = result)

    def getRequestsByVictimId(self,vid):
        requests_dao = RequestData()
        row = requests_dao.getRequestByVictimId(vid)
        if not row:
            return jsonify(Error = "Request Not Found"), 404
        else:
            result = self.build_request_dict(row)
        return jsonify(Request = result)

    def getRequestsInfoByVictimId(self, vid):
        requests_dao = RequestData()
        row = requests_dao.getRequestsInfoByVictimId(vid)
        if not row:
            return jsonify(Error = "Request Not Found"), 404
        else:
            result = self.build_request_info_dict(row)
        return jsonify(Request = result) 

    def getRequestsByResourceId(self,resid):
        requests_dao = RequestData()
        row = requests_dao.getRequestById(resid)
        if not row:
            return jsonify(Error = "Request Not Found"), 404
        else:
            result = self.build_request_dict(row)
        return jsonify(Request = result)

    def insertRequest(self, form):
        if form and len(form) == 3:
            date_submited = form['date_submited']
            resource_id = form['resource_id']
            victim_id = form['victim_id']

            if date_submited and resource_id and victim_id:
                dao = RequestData()
                request_id = dao.insert(date_submited, resource_id, victim_id)
                result = {}
                result["request_id"] = request_id
                result["date_submited"] = date_submited
                result["resource_id"] = resource_id
                result["victim_id"] = victim_id
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Malformed post request1")
        else:
            return jsonify(Error="Malformed post request2")

    def searchRequests(self, args):
        request_id = args.get('request_id')
        status = args.get('status')
        date_submitted = args.get('date_submitted')
        resource_id = args.get('resource_id')
        victim_id = args.get('victim_id')

        requests_list = []

        if len(args) == 1 and request_id:
            requests_list = self.getRequestById(request_id)
        elif len(args) == 1 and victim_id:
            requests_list = self.getRequestsByVictimId(victim_id)
        elif len(args) == 1 and resource_id:
            requests_list = self.getRequestsByResourceId(resource_id)
        else:
            return jsonify(Error="Malformed search string"), 400

        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)
