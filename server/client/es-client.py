from elasticsearch import Elasticsearch
import logging as logger


# https://elasticsearch-py.readthedocs.io/en/master/index.html
class EsClient:
    def __init__(self):
        self.es = Elasticsearch()

    def query(self):
        searchBody = {
            'query': {
                'match_all': {}
            }
        }
        res = self.es.search(index='index-name', body=searchBody)
        return res

    def createIndex(self, indexName, ignoreAlreadyExists=True):
        logger.debug('Creating index: ' + indexName)
        if ignoreAlreadyExists:
            self.es.indices.create(index=indexName, ignore=400)

    def deleteIndex(self, indexName):
        logger.debug('Deleting index: ' + indexName)
        self.es.indices.delete(index=indexName)
