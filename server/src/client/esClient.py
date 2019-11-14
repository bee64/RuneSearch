from elasticsearch import Elasticsearch
import logging as logger


# https://elasticsearch-py.readthedocs.io/en/master/index.html
class EsClient:

    def __init__(self):
        self.es = Elasticsearch({'host': 'localhost', 'port': 9200})
        self.index = 'items'

    def query(self):
        searchBody = {
            'query': {
                'match_all': {}
            }
        }
        res = self.es.search(index=self.index, body=searchBody)
        return res

    def publishItem(self, page):
        logger.debug('Publishing page: ' + page.name)
        body = {
            
        }
        self.es.index(index=self.index, doc_type="page" body=body)

    def indexExists(self):
        logger.debug('Validating index exists.')
        # self.es.index()

    def createIndex(self, ignoreAlreadyExists=True):
        logger.debug('Creating index: ' + self.index)
        settings = {
            "settings": {
                "number_of_shards": 1
                "number_of_replicas": 0
            },
            "mappings": {
                "page": {
                    "dynamic": "strict",
                    "properties": {
                        "name": {
                            "type": "text"
                        },
                        "icon": {
                            "type": "text"
                        },
                        "url": {
                            "type": "text"
                        }
                    }
                }
            }
        }
        if ignoreAlreadyExists:
            try:
                self.es.indices.create(index=self.index, ignore=400, body=settings)
                logger.debug('Successfully created index.')
            except Exception as e:
                logger.debug(str(e))

    def deleteIndex(self):
        logger.debug('Deleting index: ' + self.index)
        try:
            self.es.indices.delete(index=self.index)
            logger.debug('Successfully deleted index')
        except Exception as e:
            logger.debug(str(e))
