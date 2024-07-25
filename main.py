import sys
import traceback
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox, QTableWidgetItem
from window_prodact import UiGolf
from pathlib import Path
from database import Data
from stream_prematch import ThreadPrematch
from factory import get_stat,get_stat_gross
from worker import Worker
from stream_live import ThreadLive
from PyQt5.QtGui import QFont, QColor, QPixmap, QImage
import configparser

class ImageDialog(QMainWindow):

    def __init__(self):
        super().__init__()
        self.settings = QSettings('GrabberGolf', 'GrabberGolf')

        # Set up the user interface from Designer.
        self.ui = UiGolf()
        self.threadpool = QThreadPool()
        self.ui.setupUi(self)
        self.thread_prematch = ThreadPrematch(self)
        self.ui.pushButton.clicked.connect(self.pick_database)
        self.ui.pushButton_2.clicked.connect(self.launch_thread_prematch)
        self.ui.pushButton_5.clicked.connect(self.wrapped_clear_database)
        self.ui.pushButton_6.clicked.connect(self.launch_thread_live)
        self.ui.pushButton_4.clicked.connect(self.wrapped_click_set_pars)
        self.ui.lineEdit_4.editingFinished.connect(self.pick_url)
        self.ui.pushButton_8.clicked.connect(self.stop_thread)
        self.ui.lineEdit_6.editingFinished.connect(self.pick_url_log)

        self.set_old_values()


    def pick_database(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Выбрать базу данных', home_dir, "*.mdb")
        road_database = fname[0]
        try:
            config = configparser.ConfigParser()
            config.read('grabber_golf_settings.ini')
            config.set('DATABASE', 'road', road_database)
            with open('grabber_golf_settings.ini', 'w') as configfile:
                config.write(configfile)
        except:
            print(traceback.format_exc())
            return
        self.ui.lineEdit_3.setText(road_database)


    def stop_thread(self):
        try:
            self.mythread_2.running = False
        except:
            pass

    def pick_url(self):
        try:
            url = self.ui.lineEdit_4.text()
            config = configparser.ConfigParser()
            config.read('grabber_golf_settings.ini')
            config.set('API', 'url_export', url)
            with open('grabber_golf_settings.ini', 'w') as configfile:
                config.write(configfile)
        except:
            print(traceback.format_exc())
            return

    def pick_url_log(self):
        try:
            url = self.ui.lineEdit_6.text()
            config = configparser.ConfigParser()
            config.read('grabber_golf_settings.ini')
            config.set('API', 'url_log', url)
            with open('grabber_golf_settings.ini', 'w') as configfile:
                config.write(configfile)
        except:
            print(traceback.format_exc())
            return





    def launch_thread_prematch(self):
        if not self.thread_prematch.isRunning():
            self.thread_prematch.signal_box.connect(self.show_message_box)
            self.thread_prematch.signal_status.connect(self.change_button_status)
            self.thread_prematch.signal_player.connect(self.fill_table)
            self.thread_prematch.start()

    def set_old_values(self):
        try:
            config = configparser.ConfigParser()
            config.read('grabber_golf_settings.ini')
            url_export = config['API']['url_export']
            url_log = config['API']['url_log']

            road_database = config['DATABASE']['road']
        except:
            print(traceback.format_exc())
            return
        try:
            self.ui.lineEdit_3.setText(road_database)
            self.ui.lineEdit_4.setText(url_export)
            self.ui.lineEdit_6.setText(url_log)

        except:
            print(traceback.format_exc())

    def closeEvent(self, event):
        self.settings.setValue('url', self.ui.lineEdit_4.text())
        self.settings.setValue('road_database', self.ui.lineEdit_3.text())

    def clear_database(self):
        try:
            databasa = Data(self.ui.lineEdit_3.text())
        except:
            print(traceback.format_exc())
            self.change_button_status((self.ui.pushButton_5, 'Error', 'БД'))
            return
        try:
            databasa.clear_database()
        except:
            self.change_button_status((self.ui.pushButton_5, 'Error', 'Clear'))
        self.change_button_status((self.ui.pushButton_5, 'Finish', 'Clear'))

    def wrapped_clear_database(self):
        reply = QMessageBox.question(self, 'Подтверждение', 'Вы уверены, что хотите очистить таблицу?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.change_button_status((self.ui.pushButton_5, 'Start', 'Clear'))
        try:
            worker = Worker(self.clear_database)
            self.threadpool.start(worker)
        except:
            print(traceback.format_exc())
            self.change_button_status((self.ui.pushButton_5, 'Error', 'Clear'))

    def click_set_pars(self):
        try:
            databasa = Data(self.ui.lineEdit_3.text())
        except:
            print(traceback.format_exc())
            return
        try:
            if self.ui.radioButton.isChecked():
                res = get_stat(self.ui.lineEdit_4.text())
            else:
                res = get_stat_gross(self.ui.lineEdit_4.text())
            print(res)
            databasa.set_par_zaezd(res[0])
        except:
            self.change_button_status((self.ui.pushButton_4, 'Error', 'Set Par'))

        self.change_button_status((self.ui.pushButton_4, 'Finish', 'Set Par'))

    def wrapped_click_set_pars(self):

        self.change_button_status((self.ui.pushButton_4, 'Start', 'Set Par'))
        try:
            worker = Worker(self.click_set_pars)
            self.threadpool.start(worker)
        except:
            print(traceback.format_exc())
            self.change_button_status((self.ui.pushButton_4, 'Error', 'Set Par'))

    def launch_thread_live(self):
        try:
            if self.mythread_2.isRunning():
                self.mythread_2.terminate()
                self.mythread_2 = ThreadLive(mainwindow=self)
                self.mythread_2.signal_status.connect(self.change_button_status)
                self.mythread_2.signal_player.connect(self.update_table_stat)
                self.mythread_2.start()

            else:
                self.mythread_2 = ThreadLive(mainwindow=self)
                self.mythread_2.signal_status.connect(self.change_button_status)
                self.mythread_2.signal_player.connect(self.update_table_stat)
                self.mythread_2.start()
        except:
            self.mythread_2 = ThreadLive(mainwindow=self)
            self.mythread_2.signal_status.connect(self.change_button_status)
            self.mythread_2.signal_player.connect(self.update_table_stat)
            self.mythread_2.start()

    def change_button_status(self, item: tuple):
        if item[1] == 'Error':
            item[0].setStyleSheet(
                """ 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: black;
                font: bold 14px;
                padding: 6px;
                background-color: red;"""
            )
            item[0].setText(item[2])
        elif item[1] == 'Finish':
            item[0].setStyleSheet(
                """ 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: black;
                font: bold 14px;
                padding: 6px;
                background-color: white;"""
            )
            item[0].setText(item[2])

        elif item[1] == 'Start':
            item[0].setStyleSheet(
                """ 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: black;
                font: bold 14px;
                padding: 6px;
                background-color: green;"""
            )
            item[0].setText(item[2])

    def show_message_box(self, item: tuple):
        if item[0] == 'error':
            QMessageBox.warning(self, item[1], f"""<p>{item[2]}</p>""", QMessageBox.StandardButton.Ok)

    def fill_table(self, players: list):
        for player in players:
            try:
                row_count = self.ui.tableWidget_3.rowCount()
                self.ui.tableWidget_3.setRowCount(row_count + 1)

                self.ui.tableWidget_3.setItem(row_count, 1,
                                              QTableWidgetItem(player['player_surname'] + ' ' + player['player_name']))
                self.ui.tableWidget_3.setItem(row_count, 0, QTableWidgetItem(str(player['player_id_ext'])))

                self.ui.tableWidget_3.item(row_count, 0).setTextAlignment(Qt.AlignCenter)
                font = QFont()
                font.setWeight(QFont.Bold)
                self.ui.tableWidget_3.item(row_count, 1).setFont(font)

                for i in range(2, 20):
                    self.ui.tableWidget_3.setItem(row_count, i, QTableWidgetItem(''))
            except:
                print(traceback.format_exc())

    def update_table_stat(self, players: list):
        try:

            for player in players:
                for row in range(self.ui.tableWidget_3.rowCount()):
                    if self.ui.tableWidget_3.item(row, 0).text() == player['player_id_ext']:
                        for i in range(1, 19):
                            player_str = str(player.get(f'shot_{i}','?')) + '/' + str(player.get(f'point_{i}','0'))
                            player_str = player_str.replace('?/','')
                            if self.ui.tableWidget_3.item(row,i+1).text() != player_str:
                                self.ui.tableWidget_3.setItem(row, i + 1, QTableWidgetItem(
                                    player_str))
                                self.ui.tableWidget_3.item(row, i + 1).setTextAlignment(Qt.AlignCenter)
                                self.change_cell_color(self.ui.tableWidget_3, row, i+1)
                            else:
                                self.ui.tableWidget_3.setItem(row, i + 1, QTableWidgetItem(
                                    player_str))
                                self.ui.tableWidget_3.item(row, i + 1).setTextAlignment(Qt.AlignCenter)


                        break
        except:
            print(traceback.format_exc())

    def change_cell_color(self, table, row, column):
        try:
            item = table.item(row, column)
            item.setBackground(QColor('yellow'))

            timer = QTimer()
            timer.singleShot(10000, lambda: self.reset_cell_color(table, row, column))
        except:
            print(traceback.format_exc())

    def reset_cell_color(self, table, row, column):
        try:
            item = table.item(row, column)
            item.setBackground(QColor(187, 255, 216))
        except:
            print(traceback.format_exc())






app = QApplication(sys.argv)
window = ImageDialog()
window.show()

sys.exit(app.exec())
