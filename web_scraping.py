# -*- coding: utf-8 -*-


import requests
import re
from bs4 import BeautifulSoup


url = 'telegra.ph/Nachnem-rabotu-s-Mock-v-Python-01-26'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.81 Chrome/58.0.3029.81 Safari/537.36'
}
s = requests.Session()
s.headers.update(headers)


def load_content(url, session):
    url = 'https://{}'.format(url)
    request = session.get(url)
    return request.text


def parse_text_data(content):
    soup = BeautifulSoup(content, 'lxml')
    return soup.find('article', {'class': 'tl_article_content'}).text


def to_count_rus_letters(text):
    return len(''.join(re.findall('[А-Яа-я]+', text)))


def main():
    data = load_content(url, s)
    content = parse_text_data(data)
    print(to_count_rus_letters(content))


if __name__ == '__main__':
    main()
