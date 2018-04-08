# -*- coding: utf-8 -*-


import sys
from gui import MainWindow, QApplication


class Application(MainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        sys.exit(app.exec_())


if __name__ == '__main__':
    Application()
