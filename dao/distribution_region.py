from config.db_config import pg_config
import psycopg2
class DistributionRegionData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['host'],
                                                                    pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getDistributionRegionBySupplierId(self,supplier_id):
        cursor = self.conn.cursor()
        query = "select * from distribution_region where supplier_id=%s;"
        cursor.execute(query,(supplier_id))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getDistributionRegionById(self,distribution_region_id):
        cursor = self.conn.cursor()
        query = "select * from distribution_region where distribution_region_id=%s;"
        cursor.execute(query,(distribution_region_id,))
        result = cursor.fetchone()
        return result

    def getAllDistributionRegion(self):
        cursor = self.conn.cursor()
        query = "select * from distribution_region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getSupplierFromDistributionRegion(self,supplier_id):
        cursor = self.conn.close()
        query = "select * from distribution_region natural inner join supplier where supplier_id=%s;"
        cursor.execute(query,(supplier_id))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getRegionFromDistributionRegion(self,region_id):
        cursor = self.conn.cursor()
        query = "select * from distribution_region natural inner join region where region_id=%s;"
        cursor.execute(query,(region_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionIdAndResourceId(self,region_id, resource_id):
        cursor = self.conn.cursor()
        query = "select resource_name, resource_id, company_name, supplier_id, region_name, region_id from region natural inner join distribution_region natural inner join supplies natural inner join supplier natural inner join resource where region_id = %s and resource_id=%s and isavailable=TRUE;"
        cursor.execute(query,(region_id,resource_id))
        result = []
        for row in cursor:
            result.append(row)
        return result




