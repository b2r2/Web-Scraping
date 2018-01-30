# -*- coding: utf-8 -*-


import requests
import re
from bs4 import BeautifulSoup


class WebScraping:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.81 Chrome/58.0.3029.81 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def load_content(self, url):
        request = self.session.get(url)
        return request.text

    def parse_text_data(self, content):
        soup = BeautifulSoup(content, 'lxml')
        return soup.find('article', {'class': 'tl_article_content'}).text

    def get_rus_letters(self, text):
        rus_letters = re.findall('[А-Яа-я]+', text)
        return len(''.join(rus_letters))
