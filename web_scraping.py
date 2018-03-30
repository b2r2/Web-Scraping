# -*- coding: utf-8 -*-


import requests
import re
from bs4 import BeautifulSoup


class Scraper():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.81 Chrome/58.0.3029.81 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def __load_content(self, url):
        request = self.session.get(url, timeout=5)
        return request.text

    def __parse_text_data(self, content):
        soup = BeautifulSoup(content, 'lxml')
        soup.pre.decompose()
        soup.figure.decompose()
        return soup.find(name='article', attrs={'class': 'tl_article_content'}).text

    def __get_text_size(self, text):
        rus_letters = re.findall('[А-Яа-я]+', text)
        return len(''.join(rus_letters))

    def run(self, url):
        data = self.__load_content(url)
        content = self.__parse_text_data(data)
        return self.__get_text_size(content)
