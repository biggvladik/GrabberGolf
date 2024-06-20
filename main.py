import sys
import traceback
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox
from window import Ui_Football
from pathlib import Path
from database import Data
from stream_prematch import ThreadPrematch
from factory import get_stat
from worker import Worker


class ImageDialog(QMainWindow):

    def __init__(self):
        super().__init__()
        self.settings = QSettings('GrabberGymnastic', 'GrabberGymnastic')

        # Set up the user interface from Designer.
        self.ui = Ui_Football()
        self.threadpool = QThreadPool()
        self.ui.setupUi(self)
        self.thread_prematch = ThreadPrematch(self)
        self.ui.pushButton.clicked.connect(self.pick_database)
        self.ui.pushButton_2.clicked.connect(self.launch_thread_prematch)
        self.ui.pushButton_4.clicked.connect(self.clear_database)
        self.ui.pushButton_6.clicked.connect(self.launch_thread2)
        self.ui.pushButton_4.clicked.connect(self.wrapped_click_set_pars)
        self.set_old_values()

    def pick_database(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Выбрать базу данных', home_dir, "*.mdb")
        temp = fname[0].split('/')
        road_database = fname[0]
        try:
            databasa = Data(road_database)
        except:
            print(traceback.format_exc())
        self.ui.lineEdit_3.setText(road_database)
        self.ui.pushButton.setText(temp[-1])

    def launch_thread_prematch(self):
        if not self.thread_prematch.isRunning():
            self.thread_prematch.signal_box.connect(self.show_message_box)
            self.thread_prematch.signal_status.connect(self.change_button_status)

            self.thread_prematch.start()



    def set_old_values(self):
        try:
            self.ui.lineEdit_3.setText(self.settings.value('road_database'))
            self.ui.lineEdit_4.setText(self.settings.value('url'))
        except:
            print(traceback.format_exc())

    def closeEvent(self, event):
        self.settings.setValue('url', self.ui.lineEdit_4.text())
        self.settings.setValue('road_database', self.ui.lineEdit_3.text())

    def clear_database(self):
        database = Data(self.ui.lineEdit_3.text())
        database.clear_database()



    def click_set_pars(self):
        try:
            databasa = Data(self.ui.lineEdit_3.text())
        except:
            print(traceback.format_exc())
            return
        try:
            res = get_stat(self.ui.lineEdit_4.text())
            print(res)
            databasa.set_par_zaezd(res[0])
        except:
            self.change_button_status((self.ui.pushButton_4, 'Error', 'Set Pars'))

        self.change_button_status((self.ui.pushButton_4, 'Finish', 'Set Pars'))

    def wrapped_click_set_pars(self):

        self.change_button_status((self.ui.pushButton_4, 'Start', 'Set Pars'))
        try:
            worker = Worker(self.click_set_pars)
            self.threadpool.start(worker)
        except:
            print(traceback.format_exc())
            self.change_button_status((self.ui.pushButton_4, 'Error', 'Set Pars'))



    def launch_thread2(self):
        try:
            if self.mythread_2.isRunning():
                self.mythread_2.terminate()
                self.mythread_2 = Thread_2(mainwindow=self)
                self.mythread_2.signal_status.connect(self.change_button_status)
                self.mythread_2.start()

            else:
                self.mythread_2 = Thread_2(mainwindow=self)
                self.mythread_2.signal_status.connect(self.change_button_status)
                self.mythread_2.start()
        except:
            self.mythread_2 = Thread_2(mainwindow=self)
            self.mythread_2.signal_status.connect(self.change_button_status)
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


    def open_table_window(self):
        self.new_window = TableWindow(road = self.ui.lineEdit_3.text())
        self.new_window.show()


app = QApplication(sys.argv)
window = ImageDialog()
window.show()

sys.exit(app.exec())