import os
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from web_scraping import Scraper


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__init_ui()
        self.show()

    def __init_ui(self):
        url_button = QPushButton('Url', self)
        quit_button = QPushButton('Quit', self)
        url_input = QLineEdit(self)

        grid = QGridLayout()
        grid.setSpacing(1)
        grid.addWidget(url_input, 1, 0)
        grid.addWidget(url_button, 1, 1)
        grid.addWidget(quit_button, 2, 1)

        self.setLayout(grid)

        url_button.clicked.connect(lambda: self.__on_click(url_input.text()))
        quit_button.clicked.connect(QCoreApplication.instance().quit)

        self.__move_to_center(300, 10)
        self.setWindowTitle('Counter')
        self.setWindowIcon(QIcon('logo.png'))

    def __move_to_center(self, width, height):
        self.resize(width, height)
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

    def __on_click(self, url):
        size_text = Scraper().run(url)
        output_text = 'All Russian symbols:' + os.linesep
        message_box = QMessageBox()
        message_box.setText(output_text + str(size_text))
        message_box.setWindowTitle('Counter')
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()
