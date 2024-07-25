from PyQt5.QtCore import *
from database import Data
from factory import get_stat, get_stat_log,get_stat_gross
import traceback
import time


class ThreadLive(QThread):
    signal_status = pyqtSignal(tuple)
    signal_box = pyqtSignal(tuple)
    signal_player = pyqtSignal(list)

    def __init__(self, mainwindow, parent=None):
        QThread.__init__(self, parent)
        self.running = False
        self.mainwindow = mainwindow

    def run(self):
        self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Start', 'Live'))
        url_export = self.mainwindow.ui.lineEdit_4.text()
        url_log = self.mainwindow.ui.lineEdit_6.text()

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
                if self.mainwindow.ui.radioButton.isChecked():
                    temp_res = get_stat(url_export)
                else:
                    temp_res = get_stat_gross(url_export)
            except Exception as error:
                self.signal_box.emit(('error', 'Ошибка при запросе  к API', error))
                continue


            # Обновляем стату в Players
            try:
                data.update_score_players(temp_res[1])
            except:
                self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Error', 'SP'))
                print(traceback.format_exc())

            # Обновляем стату в ZaezdMaps
            if self.mainwindow.ui.checkBox.isChecked():
                data_score = get_stat_log(url_log,self.mainwindow.ui.comboBox.currentText())
                try:
                    data.update_score_logs(data_score)
                except:
                    self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Error', 'ZM'))
                    print(traceback.format_exc())

            self.signal_player.emit(temp_res[1])

            try:
                time.sleep(float(self.mainwindow.ui.lineEdit_5.text()))
            except:
                pass

            end = time.time() - start
            self.signal_status.emit((self.mainwindow.ui.pushButton_7, 'Finish', str(round(end, 2))))
            self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Start', 'Live'))



        self.signal_status.emit((self.mainwindow.ui.pushButton_6, 'Finish', 'Live'))
