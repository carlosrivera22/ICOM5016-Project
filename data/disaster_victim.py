from config.db_config import pg_config
import psycopg2
class DisasterVictimData:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getVictimById(self,victim_id):
        cursor = self.conn.cursor()

    def getVictimAddress(self,address_id):
        cursor = self.conn.cursor()

    def getAllVictims(self):
        cursor = self.conn.cursor()