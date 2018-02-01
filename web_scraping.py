# -*- coding: utf-8 -*-


import sys
import requests
import re
import gui
from bs4 import BeautifulSoup


class Scraper():
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

    def get_text_size(self, text):
        rus_letters = re.findall('[А-Яа-я]+', text)
        return len(''.join(rus_letters))


def on_click(url, QMessageBox):
    size_text = get_size_text(url)
    output_text = 'All Russian symbols\n'
    message_box = QMessageBox()
    message_box.setText(output_text + str(size_text))
    message_box.setWindowTitle('Counter')
    message_box.setIcon(QMessageBox.Information)
    message_box.setStandardButtons(QMessageBox.Ok)
    message_box.exec_()


def get_size_text(url):
    scraper = Scraper()
    data = scraper.load_content(url)
    content = scraper.parse_text_data(data)
    return scraper.get_text_size(content)


if __name__ == '__main__':
    app = gui.QApplication(sys.argv)
    window = gui.MainWindow()
    sys.exit(app.exec_())
