class AddressData:
    addresses = [
        {
            'address_id':1,
            'user_id':1,
            'region_id':1,
            'street':'Calle Mendez Vigo',
            'city':'Mayaguez',
            'state':'Puerto Rico',
            'country': 'USA',
            'zipcode': '00680'
        },
        {
            'address_id':2,
            'user_id':2,
            'region_id':2,
            'street':'',
            'city':'',
            'state':'',
            'country': '',
            'zipcode': ''
        },
        {
            'address_id':3,
            'user_id':3,
            'region_id':3,
            'street':'',
            'city':'',
            'state':'',
            'country': '',
            'zipcode': ''
        },
    ]

    def getAllAddresses(self):
        return self.addresses

    def getAddressById(self,aid):
        for a in self.addresses:
            if a['address_id'] == aid:
                return a
        return "No address found for specified id"

    def getAddressOfUserByUserId(self,uid):
        for a in self.addresses:
            if a['user_id'] == uid:
                return a
        return "No address found for user"

    def getAllAddressesOfARegion(self,rid):
        for a in self.addresses:
            if a['region_id'] == rid:
                return a
        return "No addresses found for this region"
