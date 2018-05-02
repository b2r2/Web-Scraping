# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from web_scraping import Scraper

class UIMainWindow:
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(240, 100)
        main_window.setMinimumSize(QtCore.QSize(240, 100))
        main_window.setMaximumSize(QtCore.QSize(240, 100))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(self.icon)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")
        self.form_layout = QtWidgets.QFormLayout(self.central_widget)
        self.form_layout.setObjectName("formLayout")
        self.line_edit = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit.setObjectName("lineEdit")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.line_edit)
        self.message_box = QtWidgets.QMessageBox()
        self.message_box.setObjectName("messageBox")
        self.message_box.setWindowTitle("Counter")
        self.result_btn = QtWidgets.QPushButton(self.central_widget)
        self.result_btn.setObjectName("Result")
        self.result_btn.clicked.connect(lambda: self.on_click(self.line_edit.text()))
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.result_btn)
        self.exit_btn = QtWidgets.QPushButton(self.central_widget)
        self.exit_btn.setObjectName("Exit")
        self.exit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.exit_btn)
        main_window.setCentralWidget(self.central_widget)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Counter"))
        self.result_btn.setText(_translate("MainWindow", "Result"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))

    def on_click(self, url):
        _size = Scraper().run(url)
        self.get_message_box(_size)

    def get_message_box(self, _size):
        self.message_box.setText(str(_size))
        self.message_box.setIcon(QtWidgets.QMessageBox.Information)
        self.message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.message_box.setWindowIcon(self.icon)
        self.message_box.show()
