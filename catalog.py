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

    def __handle_zen(self, soup):
        self.__handle_figure(soup)

    def __handle_telegraph(self, soup):
        self.__handle_pre(soup)
        self.__handle_figure(soup)

    @staticmethod
    def __handle_pre(soup):
        try:
            soup.pre.decompose()
        except AttributeError as err:
            print('<pre>: Quote not found({})'.format(err))

    @staticmethod
    def __handle_figure(soup):
        try:
            soup.figure.decompose()
        except AttributeError as err:
            print('<figure>: Picture not found({})'.format(err))
