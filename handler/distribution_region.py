class DistributionRegionHandler:
    def build_distributionregion_dict(self,row):
        result = {}
        result['distribution_region_id'] = row[0]
        result['supplier_id'] = row[1]
        result['region_id'] = row[2]


