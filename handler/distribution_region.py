from flask import Flask,jsonify
from dao.distribution_region import DistributionRegionData
class DistributionRegionHandler:
    def build_distributionregion_dict(self,row):
        result = {}
        result['resource_name'] = row[0]
        result['resource_id'] = row[1]
        result['company_name'] = row[2]
        result['supplier_id'] = row[3]
        result['region_name'] = row[4]
        result['region_id'] = row[5]
        return result

    def getResourcesByRegionIdAndResourceId(self,region_id,resource_id):
        dao = DistributionRegionData()
        region_list = dao.getResourcesByRegionIdAndResourceId(region_id,resource_id)
        result_list = []
        for row in region_list:
            result = self.build_distributionregion_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)
