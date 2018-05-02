# -*- coding: utf-8 -*-


import sys
import gui
from PyQt5 import QtWidgets


class CounterApp(QtWidgets.QMainWindow, gui.UIMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CounterApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
