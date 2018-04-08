# -*- coding: utf-8 -*-


import re
from requests import Session
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.headers = {
            'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                           ' AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu'
                           ' Chromium/58.0.3029.81 Chrome/58.0.3029.81'
                           ' Safari/537.36')
        }
        self.session = Session()
        self.session.headers.update(self.headers)
        self.parser = re.compile(r'[а-я]', re.IGNORECASE)
        self.soup = None

    def __load_content(self, url):
        request = self.session.get(url, timeout=5)
        return request.text

    def __parse_text_data(self, content, pattern):
        state = {
            'zen': self.__get_pattern_zen,
            'telegraph': self.__get_pattern_telegraph
        }
        self.soup = BeautifulSoup(content, 'lxml')
        try:
            state[pattern]()
        except AttributeError:
            print('I not found picture and/or quote!')
        return self.soup.article.get_text(separator=' ', strip=True)

    def __get_pattern_zen(self):
        self.soup.figure.decompose()

    def __get_pattern_telegraph(self):
        self.soup.pre.decompose()
        self.soup.figure.decompose()
        self.soup.article.address.decompose()

    def __get_text_size(self, text):
        handled_text = re.findall(self.parser, text)
        return len(handled_text)

    def run(self, url, pattern):
        data = self.__load_content(url)
        content = self.__parse_text_data(data, pattern)
        return self.__get_text_size(content)
