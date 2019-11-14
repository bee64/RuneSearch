from mwclient import Site


class WikiClient:
    def __init__(self):
        self.wiki = Site('oldschool.runescape.wiki', path='/')

    wiki = Site('oldschool.runescape.wiki', path='/')

    def getPages(self):
        return self.wiki.allpages()
