class DisasterVictimData:
    victims = [
        {
            'victim_id':1,
            'user_id':1,
            'address_id':1
        },
        {
            'victim_id':2,
            'user_id':2,
            'address_id':2
        },
        {
            'victim_id':3,
            'user_id':3,
            'address_id':3
        },
    ]

    def getAllDisasterVictims(self):
        return self.victims

    def getVictimById(self, vid):
        for v in self.victims:
            if v['victim_id'] == vid:
                return v
        return 'No victim found'

    def getVictimByUserId(self, uid):
        for v in self.victims:
            if v['user_id'] == uid:
                return v
        return 'No victim found'
