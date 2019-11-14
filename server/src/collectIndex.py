from client.esClient import EsClient
from client.wikiClient import WikiClient


def createIndex():
    esClient = EsClient()
    esClient.createIndex('items')


class Page:
    def __init__(self, name="", icon="", url=""):
        self.name = name
        self.icon = icon
        self.url = url


def loadWikiPages():
    wikiClient = WikiClient()
    for page in wikiClient.getPages():
        # TODO Images and url
        page = Page(name = page.name)


def run():
    createIndex()
    loadWikiPages()


run()
