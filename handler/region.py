from flask import jsonify
from data.region import RegionData

class RegionHandler:

    def getAllRegions(self):
        region = RegionData()
        return jsonify(region.getAllRegions())

    def getRegionById(self,id):
        region = RegionData()
        result = region.getRegionById(id)
        return jsonify(result)

    def getRegionByName(self,name):
        region = RegionData()
        result = region.getRegionByName(name)
        return jsonify(result)

    def searchRegion(self,args):
        region_name = args.get('region_name')
        region_id = args.get('region_id')
        if(len(args) > 1):
            return jsonify(Error="Malformed search string."), 400
        if len(args) == 1 and region_name:
            if region_name:
                data = RegionData()
                region = data.getRegionByName(region_name)
                return jsonify(region)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and region_id:
            if region_id:
                data = RegionData()
                region = data.getRegionById(int(region_id))
                return jsonify(region)
            else:
                return jsonify(Error="Malformed search string."), 400



