from config.db_config import pg_config
import psycopg2
class WeeklyStatisticData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllWeeklyStats(self):
        cursor = self.conn.cursor()

    def getWeeklyStatsByResource(self,resource_id):
        cursor = self.conn.cursor()

    def getWeeklyStatByWeek(self,week_id):
        cursor = self.conn.cursor()

    def getResourcesNeededWeeklyStats(self):
        cursor = self.conn.cursor()

    def getResourcesAvailableWeeklyStats(self):
        cursor = self.conn.cursor()

    def getResourcesResolvedWeeklyStats(self):
        cursor = self.conn.cursor()







