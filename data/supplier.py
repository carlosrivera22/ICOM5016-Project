class SupplierData:
    suppliers = [
        {
            'supplier_id': 1,
            'company_name': 'company1',
            'address_id': 11,
            'region_id': 111
        },
        {
            'supplier_id': 2,
            'company_name': 'company2',
            'address_id': 12,
            'region_id': 112
        },
        {
            'supplier_id': 3,
            'company_name': 'company3',
            'address_id': 13,
            'region_id': 111
        },
        {
            'supplier_id': 4,
            'company_name': 'company4',
            'address_id': 14,
            'region_id': 114
        },
        {
            'supplier_id': 5,
            'company_name': 'company5',
            'address_id': 14,
            'region_id': 111
        },
        {
            'supplier_id': 6,
            'company_name': 'company1',
            'address_id': 13,
            'region_id': 113
        },
        {
            'supplier_id': 7,
            'company_name': 'company3',
            'address_id': 11,
            'region_id': 112
        },
    ]


    def getAllSuppliers(self):
        return self.suppliers

    def getSupplierById(self,id):
        for s in self.suppliers:
            if s['supplier_id'] == id:
                return s
        return 'No supplier found'











