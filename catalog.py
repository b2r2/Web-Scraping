#-*- coding: utf-8 -*-


class Catalog:
    def __init__(self, pattern):
        self._catalog = {
            'zen': self.__handle_zen,
            'telegraph': self.__handle_telegraph,
        }
        if pattern in self._catalog.keys():
            self.pattern = pattern
        else:
            raise ValueError('Invalid value for Pattern: {0}'.format(pattern))

    def get_content(self, soup):
        return self._catalog[self.pattern](soup)

    @staticmethod
    def __handle_zen(soup):
        soup.figure.decompose()

    @staticmethod
    def __handle_telegraph(soup):
        soup.pre.decompose()
        soup.figure.decompose()
        soup.article.address.decompose()
