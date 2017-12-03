class RegionData:
    regions = [
        {
            'region_id': 1,
            'region_name': 'San Juan'
        },
        {
            'region_id': 2,
            'region_name': 'Bayamón'
        },
        {
            'region_id': 3,
            'region_name': 'Arecibo'
        },
        {
            'region_id': 4,
            'region_name': 'Mayagüez'
        },
        {
            'region_id': 5,
            'region_name': 'Ponce'
        },
        {
            'region_id': 6,
            'region_name': 'Guayama'
        },
        {
            'region_id': 7,
            'region_name': 'Humacao'
        },
        {
            'region_id': 8,
            'region_name': 'Carolina'
        }
    ]

    def getAllRegions(self):
        return self.regions

    def getRegionById(self,id):
        for r in self.regions:
            if r['region_id'] == id:
                return r
        return 'No region found '

    def getRegionByName(self,name):
        for r in self.regions:
            if r['region_name'] == name:
                return r
        return 'No region found'