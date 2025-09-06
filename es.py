# dal/es_dal.py
from elasticsearch import Elasticsearch
import os

class ElasticDAL:
    def __init__(self, url=None, index=None):
        self.url = url or os.getenv("ES_URL", "http://elasticsearch:9200")
        self.index = index or os.getenv("ES_INDEX", "docs")

        self.es = Elasticsearch(self.url)

    def index_doc(self, doc: dict, doc_id=None):
        return self.es.index(index=self.index, id=doc_id, document=doc)

    def search(self, query: dict):
        return self.es.search(index=self.index, query=query)

    def get_doc(self, doc_id: str):
        return self.es.get(index=self.index, id=doc_id)

    def delete_doc(self, doc_id: str):
        return self.es.delete(index=self.index, id=doc_id)
