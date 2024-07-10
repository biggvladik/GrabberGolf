from window import Ui_Football
from PyQt5 import QtCore, QtGui, QtWidgets


class UiGolf(Ui_Football):
    def retranslateUi(self, UiGolf):
        super().retranslateUi(UiGolf)
        UiGolf.setWindowTitle("GrabberGolf 1.3")

        self.tableWidget_3.setColumnWidth(0, 40)
        self.tableWidget_3.setColumnWidth(1, 150)
        for i in range(2, 20, 1):
            self.tableWidget_3.setColumnWidth(i, 40)

        self.tableWidget_3.verticalHeader().setDefaultSectionSize(5)
