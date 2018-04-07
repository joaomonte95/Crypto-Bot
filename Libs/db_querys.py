from pymongo import MongoClient

class MongoQuerys(MongoClient):
    def __init__(self):
        self.client = MongoClient('localhost',27017)

    def get_token(self,srch_filter):
        self.bank = self.client.admin
        collection = self.bank.token
        return collection.find_one(srch_filter)

    def drop_collections(self):
        self.bank = self.client.CurrencyData
        collection = self.bank.CurrencyAll
        collection.drop()

    def post_to_db(self,data):
        self.bank = self.client.CurrencyData
        collection = self.bank.CurrencyAll
        collection.insert_one(data)

    def get_from_db(self,srch_filter):
        self.bank = self.client.CurrencyData
        collection = self.bank.CurrencyAll
        return collection.find_one(srch_filter)
