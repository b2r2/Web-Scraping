#-*- coding: utf-8 -*-


class Catalog:
    def __init__(self, pattern):
        self.soup = None
        self._catalog = {
            'zen': self.__handle_zen,
            'telegraph': self.__handle_telegraph,
        }
        if pattern in self._catalog.keys():
            self.pattern = pattern
        else:
            raise ValueError('Invalid value for Pattern: {0}'.format(pattern))

    def set_soup(self, soup):
        self.soup = soup

    def get_content(self):
        return self._catalog[self.pattern]()

    def __handle_zen(self):
        self.__handle_figure()

    def __handle_telegraph(self):
        self.__handle_pre()
        self.__handle_figure()

    def __handle_pre(self):
        try:
            self.soup.pre.decompose()
        except AttributeError as err:
            print('<pre>: Quote not found({})'.format(err))

    def __handle_figure(self):
        try:
            self.soup.figure.decompose()
        except AttributeError as err:
            print('<figure>: Picture not found({})'.format(err))
