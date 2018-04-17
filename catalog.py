#-*- coding: utf-8 -*-
from utils import catch_exception


class Catalog:
    def __init__(self, pattern):
        self.soup = None
        self._catalog = {
            'zen': self.__handle_zen,
            'telegra': self.__handle_telegraph,
            'none': lambda: print('There is no pattern'),
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

    @catch_exception
    def __handle_pre(self):
        self.soup.pre.decompose()

    @catch_exception
    def __handle_figure(self):
        self.soup.figure.decompose()
