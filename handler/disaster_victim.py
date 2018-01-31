from flask import jsonify
from dao.disaster_victim import DisasterVictimData

class DisasterVictimHandler:

    def build_victim_dict(self, row):
        result = {}
        result['victim_id'] = row[0]
        result['user_id'] = row[1]
        result['address_id'] = row[2]
        return result

    def build_victim_info_dict(self, row):
        result = {}
        result['victim_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['street'] = row[3]
        result['city'] = row[4]
        result['state'] = row[5]
        result['country'] = row[6]
        result['zipcode'] = row[7]
        return result

    def build_victim_cc_info_dict(self, row):
        result = {}
        result['first_name'] = row[0]
        result['last_name'] = row[1]
        result['victim_id'] = row[2]
        result['name_on_card'] = row[3]
        result['credit_card_number'] = row[4]
        result['exp_date'] = row[5]
        result['cvs'] = row[6]
        return result

    def build_address_dict(self, row):
        result = {}
        result['address_id'] = row[0]
        result['region_id'] = row[1]
        result['street'] = row[2]
        result['country'] = row[3]
        result['city'] = row[4]
        result['zipcode'] = row[5]
        result['residence'] = row[6]
        return result

    def build_victim_attributes(self, victim_id, user_id, address_id):
        result = {}
        result['victim_id'] = victim_id
        result['user_id'] = user_id
        result['address_id'] = address_id
        return result

    def build_request_dict(self, row):
        result = {}
        result['request_id'] = row[0]
        result['resource_name'] = row[1]
        result['date_submited'] = row[2]
        result['resource_id'] = row[3]
        return result

    def build_request_complete_dict(self, row):
        result = {}
        result['request_completed_id'] = row[0]
        result['request_id'] = row[1]
        result['date_resolved'] = row[2]
        result['order_type'] = row[3]
        result['supplier_id'] = row[4]
        result['victim_id']= row[5]
        result['resource_id'] = row[6]
        result['price'] = row[7]

    def getAllDisasterVictims(self):
        victims_dao = DisasterVictimData()
        victims_list = victims_dao.getAllVictims()
        result_list = []
        for row in victims_list:
            result = self.build_victim_dict(row)
            result_list.append(result)
        return jsonify(DisasterVictims = result_list)

    def getAllDisasterVictimsInfo(self):
        victims_dao = DisasterVictimData()
        victims_list = victims_dao.getAllVictimsInfo()
        result_list = []
        for row in victims_list:
            result = self.build_victim_info_dict(row)
            result_list.append(result)
        return jsonify(DisasterVictims = result_list)

    def getVictimById(self,vid):
        victims_dao = DisasterVictimData()
        row = victims_dao.getVictimById(vid)
        if not row:
            return jsonify(Error = "Victim Not Found"), 404
        else:
            victim = self.build_victim_dict(row)
        return jsonify(DisasterVictim = victim)

    def getVictimInfoById(self,vid):
        victims_dao = DisasterVictimData()
        row = victims_dao.getVictimInfoById(vid)
        if not row:
            return jsonify(Error = "Victim Not Found"), 404
        else:
            victim = self.build_victim_info_dict(row)
        return jsonify(DisasterVictim = victim)

    def getVictimCreditCard(self, vid):
        victims_dao = DisasterVictimData()
        victims_list = victims_dao.getVictimCreditCard(vid)
        result_list = []
        for row in victims_list:
            result = self.build_victim_cc_info_dict(row)
            result_list.append(result)
        return jsonify(DisasterVictims = result_list)

    def getVictimByUserId(self,uid):
        victims_dao = DisasterVictimData()
        row = victims_dao.getVictimByUserId(uid)
        if not row:
            return jsonify(Error = "Victim Not Found"), 404
        else:
            victim = self.build_victim_dict(row)
        return jsonify(DisasterVictim = victim)

    def searchVictims(self, args):
        victim_id = args.get('victim_id')
        user_id = args.get('user_id')
        address_id = args.get('address_id')
        victims_dao = DisasterVictimData()
        victims_list = []

        if len(args) == 1 and victim_id:
            victims_list = victims_dao.getVictimById(victim_id)
        elif len(args) == 1 and user_id:
            victims_list = victims_dao.getVictimByUserId(user_id)
        else:
            return jsonify(Error = "Malformed search string"), 400
        result_list = []
        for row in victims_list:
            result = self.build_victim_dict(row)
            result_list.append(result)
        return jsonify(DisasterVictims = result_list)

    def getRequestsByVictimId(self, victim_id):
        dao = DisasterVictimData()
        if not dao.getVictimById(victim_id):
            return jsonify(Error="Victim Not Found"), 404
        request_list = dao.getRequestedByVictimId(victim_id)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestCompleteByVictimId(self, victim_id):
        dao = DisasterVictimData()
        if not dao.getVictimById(victim_id):
            return jsonify(Error="Victim Not Found"), 404
        request_completed_list = dao.getRequestedByVictimId(victim_id)
        result_list = []
        for row in request_completed_list:
            result = self.build_request_complete_dict(row)
            result_list.append(result)
        return jsonify(Request_Completed=result_list)

    def insertVictim(self, form):
        if form and len(form) == 12:
            first_name = form['first_name']
            last_name = form['last_name']
            email = form['email']
            phone = form['phone']
            password = form['password']
            confirm_password = form['confirm_password']
            street = form['street']
            region_id = form['region_id']
            city = form['city']
            state = form['state']
            country = form['country']
            zipcode = form['zipcode']

            if first_name and last_name and email and phone and password and confirm_password and street and region_id and city and state and country and zipcode:
                dao = DisasterVictimData()
                victim_id = dao.insert(first_name, last_name, email, phone, password, confirm_password, street,
                                       region_id, city, state, country, zipcode)
                result = {}
                result["first_name"] = first_name
                result["last_name"] = last_name
                result["email"] = email
                result["phone"] = phone
                result["password"] = password
                result["confirm_password"] = confirm_password
                result["street"] = street
                result["region_id"] = region_id
                result["city"] = city
                result["state"] = state
                result["country"] = country
                result["zipcode"] = zipcode
                return jsonify(Victim=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")
