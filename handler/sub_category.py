from flask import jsonify
from dao.sub_category import SubCategoryData

class SubCategoryHandler:
    def build_subcategory_dict(self,row):
        result = {}
        result['subcategory_id'] = row[0]
        result['subcategory_name'] = row[1]
        result['category_id'] = row[2]
        return result

    def build_category_dict(self,row):
        result = {}
        result['category_id'] = row[0]
        result['category_name'] = row[1]
        return result

    def getAllSubCategories(self):
        data = SubCategoryData()
        subcategory_list = data.getAllSubcategories()
        result_list = []
        for row in subcategory_list:
            result = self.build_subcategory_dict(row)
            result_list.append(result)
        return jsonify(Subcategories=result_list)

    def getSubCategoryById(self, sub_category_id):
        data = SubCategoryData()
        row = data.getSubCategoryById(sub_category_id)
        if not row:
            return jsonify(Error="Subcategory Not Found"),404
        else:
            subcategory = self.build_subcategory_dict(row)
        return jsonify(Subcategory=subcategory)

    def getSubCategoryByCategoryId(self, category_id):
        data= SubCategoryData()
        subcategory_list = data.getSubCategoryByCategoryId(category_id)
        result_list = []
        for row in subcategory_list:
            result = self.build_subcategory_dict(row)
            result_list.append(result)
        return jsonify(Subcategories=result_list)


    def getCategoryFromSubcategoryId(self,subcategory_id):
        data = SubCategoryData()
        if not data.getSubCategoryById(subcategory_id):
            return jsonify(Error="Subcategory not found"),404
        subcategory_list = data.getCategoryFromSubcategoryId(subcategory_id)
        result_list = []
        for row in subcategory_list:
            result = self.build_category_dict(row)
            result_list.append(result)
        return jsonify(SubcategoryCategory=result_list)

    #FALTA ESTO
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


