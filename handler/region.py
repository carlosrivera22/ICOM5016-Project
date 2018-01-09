from flask import jsonify
from dao.region import RegionDAO


class RegionHandler:

    def build_region_dict(self,row):
        result = {}
        result['region_id'] = row[0]
        result['region_name'] = row[1]
        result['region_number'] = row[2]
        return result

    def build_region_attributes(self, region_id, region_name, region_number):
        result = {}
        result['region_id'] = region_id
        result['region_name'] = region_name
        result['region_number'] = region_number
        return result

    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['category_id'] = row[1]
        result['resource_name'] = row[2]
        result['isavailable'] = row[3]
        result['isneeded'] = row[4]
        result['quantity'] = row[5]
        result['keyword'] = row[6]
        return result

    def getAllRegion(self):
        dao = RegionDAO()
        region_list = dao.getAllRegion()
        result_list = []
        for row in region_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Regions=result_list)

    def getRegionById(self, region_id):
        dao = RegionDAO()
        row = dao.getRegionById(region_id)
        if not row:
            return jsonify(Error="Region Not Found"), 404
        else:
            region = self.build_region_dict(row)
            return jsonify(Region=region)

    def searchRegions(self, args):
        region_name = args.get("region_name")
        region_number = args.get("region_number")
        dao = RegionDAO()
        regions_list = []

        if (len(args) == 1) and region_name:
            regions_list = dao.getRegionByRegionName(region_name)
        elif (len(args) == 1) and region_number:
            regions_list = dao.getRegionByRegionNumber(region_number)
        elif (len(args) == 2) and region_name and region_number:
            regions_list = dao.getRegionByRegionNameAndRegionNumber(region_name, region_number)
        else:
            return jsonify(Error="Malformed query string"), 400

        result_list = []
        for row in regions_list:
            result = self.build_region_dict(row)
            regions_list.append(result)
        return jsonify(Region=result_list)

    def getResourcesBySRegionId(self, region_id):
        dao = RegionDAO()
        if not dao.getRegionById(region_id):
            return jsonify(Error="Reggion  Not Found"), 404
        resources_list = dao.getResourcesByRegionId(region_id)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)