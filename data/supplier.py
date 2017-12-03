from data.region import RegionData
class SupplierData:
    suppliers = [
        {
            'supplier_id': 1,
            'company_name': 'company1',
            'address_id': 11,
            'region_id': 1
        },
        {
            'supplier_id': 2,
            'company_name': 'company2',
            'address_id': 12,
            'region_id': 2
        },
        {
            'supplier_id': 3,
            'company_name': 'company3',
            'address_id': 13,
            'region_id': 1
        },
        {
            'supplier_id': 4,
            'company_name': 'company4',
            'address_id': 14,
            'region_id': 4
        },
        {
            'supplier_id': 5,
            'company_name': 'company5',
            'address_id': 14,
            'region_id': 1
        },
        {
            'supplier_id': 6,
            'company_name': 'company1',
            'address_id': 13,
            'region_id': 3
        },
        {
            'supplier_id': 7,
            'company_name': 'company3',
            'address_id': 11,
            'region_id': 2
        },
    ]

    def getAllSuppliers(self):
        return self.suppliers

    def getSupplierById(self,sid):
        for s in self.suppliers:
            if s['supplier_id'] == sid:
                return s
        return 'No supplier found'

    def getSuppliersByRegion(self,region_name):
        region_data = RegionData()
        region = region_data.getRegionByName(region_name)
        id = region['region_id']
        result = []
        for s in self.suppliers:
            if s['region_id'] == id:
                result.append(s)
        return result


    def getSuppliersByRegionId(self,region_id):
        results = []
        for s in self.suppliers:
            if s['region_id'] == region_id:
                results.append(s)
        return results










