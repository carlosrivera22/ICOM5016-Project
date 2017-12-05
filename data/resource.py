class ResourceData:
    resources = [
        {
           'resource_name':'Dasani',
            'is_available': True,
            'is_needed': True,
            'quantity': 300,
            'keyword':'water',
            'category_id': 1
        },
        {
            'resource_name': 'Nikini',
            'is_available': True,
            'is_needed': False,
            'quantity': 500,
            'keyword': 'water',
            'category_id': 1
        },
        {
            'resource_name': 'Advil',
            'is_available': False,
            'is_needed': True,
            'quantity': 100,
            'keyword': 'medication',
            'category_id': 2
        },
        {
            'resource_name': 'Puma',
            'is_available': False,
            'is_needed': False,
            'quantity': 0,
            'keyword': 'fuel',
            'category_id': 7
        },
        {
            'resource_name': 'Empire Gas',
            'is_available': True,
            'is_needed': False,
            'quantity': 5000,
            'keyword': 'fuel',
            'category_id': 7
        },
        {
            'resource_name': 'Tito Gas',
            'is_available': True,
            'is_needed': True,
            'quantity': 2000,
            'keyword': 'fuel',
            'category_id': 7
        },
        {
            'resource_name': 'Panadol',
            'is_available': True,
            'is_needed': True,
            'quantity': 150,
            'keyword': 'medication',
            'category_id': 2
        },

    ]

    def getResources(self):
        return self.resources

    def getResourcesByName(self,resource_name):
        for r in self.resources:
            if r['resource_name'] == resource_name:
                return r
            return 'No Resource found'

    def getAvailableResources(self):
        result = []
        for r in self.resources:
            if r['is_available'] == True:
                result.append(r)

    def getNeededResources(self):
        result = []
        for r in self.resources:
            if r['is_needed'] == True:
                result.append(r)
