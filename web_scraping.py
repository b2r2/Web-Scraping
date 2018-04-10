# -*- coding: utf-8 -*-


import re
from requests import Session
from bs4 import BeautifulSoup
from catalog import Catalog


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

    def __load_content(self, url):
        request = self.session.get(url, timeout=5)
        return request.text

    @staticmethod
    def __parse_text_data(content, pattern):
        soup = BeautifulSoup(content, 'lxml')
        catalog = Catalog(pattern)
        catalog.get_content(soup)
        return soup.article.get_text(separator=' ', strip=True)

    def __get_text_size(self, text):
        text = re.findall(self.parser, text)
        return len(text)


    def run(self, url):
        pattern = 'zen' if 'zen' in url else 'telegraph'
        data = self.__load_content(url)
        content = self.__parse_text_data(data, pattern)
        return self.__get_text_size(content)
