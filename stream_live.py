from PyQt5.QtCore import *
from database import Data
from factory import get_stat
import traceback
import time

class ThreadLive(QThread):
    signal_status = pyqtSignal(tuple)
    signal_box = pyqtSignal(tuple)
    def __init__(self, mainwindow, parent=None):
        QThread.__init__(self, parent)
        self.running = False
        self.mainwindow = mainwindow

    def run(self):
        self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Start', 'Live'))
        url = self.mainwindow.ui.lineEdit_4.text()
        try:
            data = Data(self.mainwindow.ui.lineEdit_3.text())
        except Exception as error:
            self.signal_box.emit(('error', 'Ошибка при подключении к БД', error))
            return

        self.running = True
        while self.running:
            start = time.time()
            # Получаем всю инфу
            try:
                temp_res = get_stat(url)
            except Exception as error:
                self.signal_box.emit(('error', 'Ошибка при запросе  к API', error))
                continue
            print('Время запроса',round(time.time() - start,2))
            # Обновляем стату в Players
            try:
                data.update_score_players(temp_res[1])
            except:
                self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Error', 'SP'))
                print(traceback.format_exc())
            print('Время Players',round(time.time() - start,2))

            # Обновляем стату в ZaezdMaps
            try:
                data.update_zaezdmaps_score(temp_res[1])
            except:
                self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Error', 'ZM'))
                print(traceback.format_exc())
            end = time.time() - start
            self.signal_status.emit((self.mainwindow.ui.pushButton_7, 'Finish', str(round(end,2))))
            self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Start', 'Live'))
