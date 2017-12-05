class SubCategoryData:
    sub_categories = [

        {
            'sub_category_id': 1,
            'sub_category_name': 'small bottles',
            'category_id': 1,

        },

        {
            'sub_category_id': 2,
            'sub_category_name': '1 gallon bottles',
            'category_id': 1,

        },

        {
            'sub_category_id': 3,
            'sub_category_name': 'diesel',
            'category_id': 7,

        },

        {
            'sub_category_id': 4,
            'sub_category_name': 'propane',
            'category_id': 7,

        },

        {
            'sub_category_id': 5,
            'sub_category_name': 'gasoline',
            'category_id': 7,

        },

    ]

    def getSubCategories(self):
        return self.sub_categories

    def getSubCategoryById(self, sub_category_id):
        for s in self.sub_categories:
            if s['sub_category_id'] ==  sub_category_id:
                return s
        return 'No SubCategory Found'

    def getSubCategoryByName(self, sub_category_name):
        for s in self.sub_categories:
            if s['sub_category_name'] ==  sub_category_name:
                return s
        return 'No SubCategory Found'

    def getSubCategoryByCategoryId(self, category_id):
        results = []
        for s in self.sub_categories:
            if s['category_id'] == category_id:
                results.append(s)
        return results