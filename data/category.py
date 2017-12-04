class Category:
    categories = [

        {
            'category_id': 1,
            'category_name': 'Water'
        },

        {
            'category_id': 2,
            'category_name': 'Medications'
        },

        {
            'category_id': 3,
            'category_name': 'Baby Food'
        },

        {
            'category_id': 4,
            'category_name': 'Canned Food'
        },

        {
            'category_id': 5,
            'category_name': 'Dry Food'
        },

        {
            'category_id': 6,
            'category_name': 'Ice'
        },

        {
            'category_id': 7,
            'category_name': 'Fuel'
        },

        {
            'category_id': 8,
            'category_name': 'Medical Devices'
        },

        {
            'category_id': 9,
            'category_name': 'Heavy Equipment'
        },

        {
            'category_id': 10,
            'category_name': 'Tools'
        },

        {
            'category_id': 11,
            'category_name': 'Clothing'
        },

        {
            'category_id': 12,
            'category_name': 'Power Generators'
        },

        {
            'category_id': 13,
            'category_name': 'Batteries'
        },
    ]

    def getCategories(self):
        return self.categories;

    def getCategoriesByName(self, category_name):
        for c in self.categories:
            if c['category_name'] == category_name:
                return c
        return 'No Category Found'