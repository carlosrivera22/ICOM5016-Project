from flask import jsonify
from data.disaster_victim import DisasterVictimData

class DisasterVictimHandler:

    def getAllDisasterVictims(self):
        victim_data = DisasterVictimData()
        return jsonify(victim_data.getAllDisasterVictims())
