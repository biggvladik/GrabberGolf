from PyQt5.QtCore import *
from database import Data
from factory import get_stat
import traceback
import pyodbc


class ThreadPrematch(QThread):
    signal_status = pyqtSignal(tuple)
    signal_box = pyqtSignal(tuple)
    def __init__(self, mainwindow, parent=None):
        QThread.__init__(self, parent)
        self.running = False
        self.mainwindow = mainwindow

    def run(self):
        self.signal_status.emit(((self.mainwindow.ui.pushButton_2, 'Start', 'Prematch')))
        url = self.mainwindow.ui.lineEdit_4.text()
        try:
            data = Data(self.mainwindow.ui.lineEdit_3.text())
        except Exception as error:
            self.signal_box.emit(('error', 'Ошибка при подключении к БД', error))
            return

        # Получаем всю инфу
        try:
            temp_res = get_stat(url)
        except Exception as error:
            self.signal_box.emit(('error', 'Ошибка при запросе  к API', error))
            return


        # Вставляем игроков в Players
        try:
            data.insert_player(temp_res[1])
        except Exception as error:
            print(traceback.format_exc())
            self.signal_box.emit(('error', 'Ошибка при вставке в Players', error))


        # Вставляем игроков в ZaezdMaps
        try:
            data.insert_in_zaezdMaps(temp_res[1])
        except  Exception as error:
            self.signal_box.emit(('error', 'Ошибка при вставке в ZaezdMaps', error))


        self.signal_status.emit(((self.mainwindow.ui.pushButton_2, 'Finish', 'Prematch')))
