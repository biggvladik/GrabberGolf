# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Football(object):
    def setupUi(self, Football):
        Football.setObjectName("Football")
        Football.resize(1018, 811)
        Football.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(Football)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 50, 259, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3 {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"    background-color: white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    background-color: white;\n"
"}\n"
"QPushButton#pushButton:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"\n"
"\n"
"        \n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 140, 81, 31))
        self.pushButton_6.setStyleSheet("QPushButton#pushButton_6 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"    background-color: white;\n"
"}\n"
"QPushButton#pushButton_6:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"\n"
"\n"
"        \n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 140, 0, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(0, 0))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 100, 241, 16))
        self.label_6.setStyleSheet("font: bold 14px;\n"
"color: red;\n"
"  \n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 271, 31))
        self.label_7.setStyleSheet("font: bold 14px;\n"
"color:rgb(255, 0, 0);\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 20, 341, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 140, 91, 31))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    background-color: white;\n"
"}\n"
"QPushButton#pushButton_2:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"\n"
"\n"
"        \n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 140, 81, 31))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    background-color: white;\n"
"}\n"
"QPushButton#pushButton_4:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"\n"
"\n"
"        \n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 100, 341, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet("font: bold 14px;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setStyleSheet("border : 2px solid black;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(920, 10, 81, 31))
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    background-color: white;\n"
"}\n"
"QPushButton#pushButton_5:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"\n"
"\n"
"        \n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(920, 50, 81, 31))
        self.pushButton_7.setStyleSheet("QPushButton#pushButton_7 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"        \n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(30, 180, 921, 611))
        self.tableWidget_3.setStyleSheet("QTableWidget {\n"
"                background-color: rgb(187, 255, 216);\n"
"                border: 1px solid black;\n"
"            }\n"
"QHeaderView::section {\n"
"                background-color: rgb(85, 170, 127);\n"
"                color: #333;\n"
"                border: none;\n"
"                font: bold 12px;\n"
"            }")
        self.tableWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(20)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(19, item)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.verticalHeader().setHighlightSections(True)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(910, 90, 101, 17))
        self.checkBox.setStyleSheet("font: bold 14px;")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(310, 140, 81, 31))
        self.pushButton_8.setStyleSheet("QPushButton#pushButton_8 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"    background-color: white;\n"
"}\n"
"QPushButton#pushButton_8:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"\n"
"\n"
"        \n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(770, 20, 111, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setStyleSheet("font: bold 14px;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_5.setStyleSheet("border : 2px solid black;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(770, 50, 71, 22))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"\n"
"}\n"
":editable {\n"
"    background: white;\n"
"}\n"
"QComboBox:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        Football.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Football)
        self.statusbar.setObjectName("statusbar")
        Football.setStatusBar(self.statusbar)

        self.retranslateUi(Football)
        QtCore.QMetaObject.connectSlotsByName(Football)

    def retranslateUi(self, Football):
        _translate = QtCore.QCoreApplication.translate
        Football.setWindowTitle(_translate("Football", "MainWindow"))
        self.pushButton_3.setText(_translate("Football", "DATABASE"))
        self.pushButton.setText(_translate("Football", "Connect"))
        self.pushButton_6.setText(_translate("Football", "Live"))
        self.pushButton_2.setText(_translate("Football", "PreMatch"))
        self.pushButton_4.setText(_translate("Football", "Set Par"))
        self.label_2.setText(_translate("Football", "URL"))
        self.pushButton_5.setText(_translate("Football", "Clear"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Football", "#"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Football", "Игрок"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Football", "1"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Football", "2"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Football", "3"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("Football", "4"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("Football", "5"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("Football", "6"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("Football", "7"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("Football", "8"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("Football", "9"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("Football", "10"))
        item = self.tableWidget_3.horizontalHeaderItem(12)
        item.setText(_translate("Football", "11"))
        item = self.tableWidget_3.horizontalHeaderItem(13)
        item.setText(_translate("Football", "12"))
        item = self.tableWidget_3.horizontalHeaderItem(14)
        item.setText(_translate("Football", "13"))
        item = self.tableWidget_3.horizontalHeaderItem(15)
        item.setText(_translate("Football", "14"))
        item = self.tableWidget_3.horizontalHeaderItem(16)
        item.setText(_translate("Football", "15"))
        item = self.tableWidget_3.horizontalHeaderItem(17)
        item.setText(_translate("Football", "16"))
        item = self.tableWidget_3.horizontalHeaderItem(18)
        item.setText(_translate("Football", "17"))
        item = self.tableWidget_3.horizontalHeaderItem(19)
        item.setText(_translate("Football", "18"))
        self.checkBox.setText(_translate("Football", "ZaezdMaps"))
        self.pushButton_8.setText(_translate("Football", "Stop"))
        self.label_3.setText(_translate("Football", "TimeOut,s"))
        self.lineEdit_5.setText(_translate("Football", "1"))
        self.comboBox.setItemText(0, _translate("Football", "all"))
        self.comboBox.setItemText(1, _translate("Football", "10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Football = QtWidgets.QMainWindow()
    ui = Ui_Football()
    ui.setupUi(Football)
    Football.show()
    sys.exit(app.exec_())
