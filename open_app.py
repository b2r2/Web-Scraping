import sys
import web_scraping
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


class OpenApp(QWidget):
    def __init__(self, app, scaping):
        super().__init__()
        self.app = app
        self.scaping = scaping
        self.__init_ui()

    def __init_ui(self):
        self.url_button = self.__create_button('url')
        self.quit_button = self.__create_button('Quit')

        self.url_edit = QLineEdit(self)

        self.url_button.clicked.connect(self.on_click)
        self.__set_layout()
        self.__close_app()

    def __set_layout(self):
        grid = QGridLayout()
        grid.setSpacing(1)

        grid.addWidget(self.url_edit, 1, 0)
        grid.addWidget(self.url_button, 1, 1)
        grid.addWidget(self.quit_button, 2, 1)

        self.setLayout(grid)
        self.__set_center(300, 10)
        self.setWindowTitle('Counter')
        self.setWindowIcon(QIcon('logo.png'))
        self.show()

    def __create_button(self, name):
        button = QPushButton(name, self)
        return button

    def __close_app(self):
        self.quit_button.clicked.connect(QCoreApplication.instance().quit)

    def __set_center(self, x, y):
        self.resize(x, y)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def on_click(self):
        result = self.url_edit.text()
        QMessageBox.question(self, 'Counter', 'All Russian symbols:\n' + result,
                             QMessageBox.Ok, QMessageBox.Ok)
        self.url_edit.setText('')

    def run(self):
        sys.exit(self.app.exec_())


def main():
    scaping = web_scraping.WebScraping()
    app = OpenApp(QApplication(sys.argv), scaping)
    app.run()


if __name__ == '__main__':
    main()
