from client import EsClient, WikiClient


def createIndex():
    esClient = EsClient()
    esClient.createIndex('items')


def loadWikiPages():
    wikiClient = WikiClient()
    for page in wikiClient.getPages():
        print(page)
        # Create page model:
        #   Name, url, icon?


def run():
    # createIndex()
    loadWikiPages()


run()
