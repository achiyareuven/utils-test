# dal/mongo_dal.py
from pymongo import MongoClient
import os

class MongoDAL:
    def __init__(self, url=None, db_name=None, collection=None):
        self.url = url or os.getenv("MONGO_URL", "mongodb://mongo:27017/appdb")
        self.db_name = db_name or os.getenv("MONGO_DB", "appdb")
        self.collection_name = collection or os.getenv("MONGO_COLLECTION", "docs")

        self.client = MongoClient(self.url)
        self.db = self.client[self.db_name]
        self.col = self.db[self.collection_name]

    def insert_one(self, doc: dict):
        return self.col.insert_one(doc).inserted_id

    def find(self, query: dict = None):
        return list(self.col.find(query or {}))

    def update_one(self, query: dict, new_values: dict):
        return self.col.update_one(query, {"$set": new_values})

    def delete_one(self, query: dict):
        return self.col.delete_one(query)

    def close(self):
        self.client.close()
