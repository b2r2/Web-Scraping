# -*- coding: utf-8 -*-


import requests
import re
from bs4 import BeautifulSoup


article = 'Ispolzovanie-regulyarnyh-vyrazhenij-v-Python-dlya-novichkov-08-04'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.81 Chrome/58.0.3029.81 Safari/537.36'
}
s = requests.Session()
s.headers.update(headers)


def load_content(article, session):
    url = 'https://telegra.ph/{}'.format(article)
    request = session.get(url)
    return request.text


def parse_text_datafile(content):
    soup = BeautifulSoup(content, 'lxml')
    content_text = soup.find_all('div', {'class': 'tl_page'})

    return content_text


def to_count_rus_letters(text):
    return len(''.join(re.findall('[А-Яа-я]+', text.decode('utf-8'))))


def main():
    data = load_content(article, s)
    content = parse_text_datafile(data)
    print(to_count_rus_letters(content))


if __name__ == '__main__':
    main()
