#-*- coding: utf-8 -*-


class Patterner:
    def __init__(self):
        self.patterns = {
            'zen': self.__handle_zen,
            'telegraph': self.__handle_telegraph,
        }

    def get_content(self, pattern):
        return self.patterns[pattern]()

    def __handle_zen(self):
        self.soup.figure.decompose()

    def __handle_telegraph(self):
        self.soup.pre.decompose()
        self.soup.figure.decompose()
        self.soup.article.address.decompose()
