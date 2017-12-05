from flask import jsonify
from data.category import CategoryData

class CategoryHandler:

    def getAllCategories(self):
        category = CategoryData()
        return jsonify(category.getCategories())

    def getCategoryById(self, category_id):
        category = CategoryData()
        result = category.getCategoryById(category_id)
        return jsonify(result)

    def getCategoryByName(self, category_name):
        category = CategoryData()
        result = category.getCategoryByName(category_name)
        return jsonify(result)

    def searchCategory(self, args):
        category_id = args.get['category_id']
        category_name = args.get['category_name']

        if len(args) == 1 and category_id:
            if category_id:
                return self.getCategoryById(int(category_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and category_name:
            if category_name:
                return self.getCategoryByName(category_name)
            else:
                return jsonify(Error="Malformed search string."), 400
        else:
            return jsonify(Error="Malformed search string"), 400


