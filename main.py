# -*- coding: utf-8 -*-


import sys
import gui


if __name__ == '__main__':
    app = gui.QApplication(sys.argv)
    window = gui.MainWindow()
    sys.exit(app.exec_())
