from flask import jsonify
from data.sub_category import SubCategoryData

class SubCategoryHandler:

    def getAllSubCategories(self):
        sub_category = SubCategoryData()
        return jsonify(sub_category.getSubCategories())

    def getSubCategoryById(self, sub_category_id):
        sub_category = SubCategoryData()
        result = sub_category.getSubCategoryById(sub_category_id)
        return jsonify(result)

    def getSubCategoryByName(self, sub_category_name):
        sub_category = SubCategoryData()
        result = sub_category.getSubCategoryByName(sub_category_name)
        return jsonify(result)

    def getSubCategoryByCategoryId(self, category_id):
        sub_category = SubCategoryData()
        result = sub_category.getSubCategoryByCategoryId(category_id)
        return jsonify(result)

    def searchSubCategory(self, args):
        sub_category_id = args.get['sub_category_id']
        sub_category_name = args.get['sub_category_name']
        category_id = args.get['category_id']

        if len(args) == 1 and sub_category_id:
            if sub_category_id:
                return self.getSubCategoryById(int(sub_category_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and sub_category_name:
            if sub_category_name:
                return self.getSubCategoryByName(sub_category_name)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and category_id:
            if category_id:
                return self.getSubCategoryByCategoryId(category_id)
            else:
                return jsonify(Error="Malformed search string."), 400
        else:
            return jsonify(Error="Malformed search string"), 400


