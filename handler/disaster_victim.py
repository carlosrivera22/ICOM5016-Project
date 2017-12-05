from flask import jsonify
from data.disaster_victim import DisasterVictimData

class DisasterVictimHandler:

    def getAllDisasterVictims(self):
        victim_data = DisasterVictimData()
        return jsonify(victim_data.getAllDisasterVictims())

    def getVictimById(self,vid):
        victim_data = DisasterVictimData()
        return jsonify(victim_data.getVictimById(vid))

    def getVictimByUserId(self,uid):
        victim_data = DisasterVictimData()
        return jsonify(victim_data.getVictimByUserId(uid))

    def searchVictims(self,args):
        victim_id = args.get('victim_id')
        user_id = args.get('user_id')
        address_id = args.get('address_id')

        if len(args) == 1 and victim_id:
            if victim_id:
                return self.getVictimById(int(victim_id))
            else:
                return jsonify(Error="Malformed search string"), 400
        elif len(args) == 1 and user_id:
            if user_id:
                return self.getVictimByUserId(int(user_id))
            else:
                return jsonify(Error="Malformed search string"), 400
        else:
            return jsonify(Error="Malformed search string"), 400
