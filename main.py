# -*- coding: utf-8 -*-


import sys
from gui import MainWindow, QApplication
from web_scraping import Scraper


class RunApp(MainWindow, Scraper):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        sys.exit(app.exec_())


if __name__ == '__main__':
    RunApp()
