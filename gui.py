import os
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from web_scraping import Scraper


class MainWindow(QWidget, Scraper):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()
        self.web_site = 'telegraph'

    def __init_ui(self):
        url_button = QPushButton('Get', self)
        quit_button = QPushButton('Quit', self)
        url_input = QLineEdit(self)

        label = QLabel('Select your website')
        tlg_button = QRadioButton('telegraph', self)
        zen_button = QRadioButton('zen', self)
        tlg_button.setChecked(True)

        self.ratio_button_group = QButtonGroup()
        self.ratio_button_group.addButton(zen_button)
        self.ratio_button_group.addButton(tlg_button)

        grid = QGridLayout()
        grid.setSpacing(1)
        grid.addWidget(url_input, 1, 0)
        grid.addWidget(url_button, 1, 1)
        grid.addWidget(quit_button, 4, 1)
        grid.addWidget(label, 2, 0)
        grid.addWidget(tlg_button, 3, 0)
        grid.addWidget(zen_button, 4, 0)

        self.setLayout(grid)

        self.ratio_button_group.buttonClicked.connect(self.__on_ratio_button_clicked)
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
        size_text = super().run(url=url, pattern=self.web_site)
        message = 'All Russian symbols:' + os.linesep
        message_box = self.__get_message_box(message, str(size_text))
        message_box.exec_()

    def __on_ratio_button_clicked(self, button):
        self.web_site = button.text()

    def __get_message_box(self, message, size_text):
        message_box = QMessageBox()
        message_box.setText(message + size_text)
        message_box.setWindowTitle('Counter')
        message_box.setWindowIcon(QIcon('logo.png'))
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        return message_box
