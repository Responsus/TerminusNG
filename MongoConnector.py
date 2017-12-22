
import pymongo

class MongoConnector(object):
    def __init__(self):
        self.client = pymongo.MongoClient("127.0.0.1")
        self.db = self.client["terminus"]

    def get_connection(self):
        return self.db