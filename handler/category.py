from flask import jsonify
from dao.category import CategoryData

class CategoryHandler:

    def build_category_dict(self,row):
        result = {}
        result['category_id'] = row[0]
        result['category_name'] = row[1]
        return result

    def build_subcategory_dict(self,row):
        result = {}
        result['subcategory_id'] = row[0]
        result['subcategory_name'] = row[1]
        result['category_id'] = row[2]
        return result


    def getAllCategories(self):
        data = CategoryData()
        category_list = data.getAllCategories()
        result_list = []
        for row in category_list:
            result = self.build_category_dict(row)
            result_list.append(result)
        return jsonify(Categories=result_list)

    def getCategoryById(self, category_id):
        data = CategoryData()
        row = data.getCategoryById(category_id)
        if not row:
            return jsonify(Error="Category Not Found"),404
        else:
            category = self.build_category_dict(row)
        return jsonify(Category=category)


    def getCategoryByName(self, category_name):
        data = CategoryData()
        row = data.getCategoryByName(category_name)
        if not row:
            return jsonify(Error="Category Not Found"),404
        else:
            category = self.build_category_dict(row)
        return jsonify(Category=category)



    def getSubcategoriesFromCategoryId(self,category_id):
        data = CategoryData()
        if not data.getSubcategoriesFromCategoryId(category_id):
            return jsonify(Error="Category Not Found"),404
        subcategory_list = data.getSubcategoriesFromCategoryId(category_id)
        result_list = []
        for row in subcategory_list:
            result = self.build_subcategory_dict(row)
            result_list.append(result)
        return jsonify(SubcategoriesCategory=result_list)

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


