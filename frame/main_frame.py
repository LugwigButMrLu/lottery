import os
import random

from PySide2.QtCore import QTimer, QUrl, Qt
from PySide2.QtGui import QPixmap, QBrush, QPainter
from PySide2.QtMultimedia import QMediaContent, QMediaPlayer
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import DisplayLabel
from qtpy import QtWidgets

from func.global_value import gv
from ui.ui_main import Ui_MainWindow


def find_all_labels(widget):
    """递归遍历所有控件，返回所有 QLabel 控件的列表"""
    labels = []
    for child in widget.findChildren(QWidget):
        if isinstance(child, DisplayLabel) or isinstance(child, QLabel):
            labels.append(child)
        # 递归遍历子控件
        labels.extend(find_all_labels(child))
    return labels


class MainWindowFrame(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowFrame, self).__init__()
        self.setupUi(self)
        self.level = 0
        gv.init()
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint| Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.player = QMediaPlayer()
        self.prize_list = []
        self.timer_count = 0
        self.stop_flag = False
        self.lottery_status = [False, False, False, False]
        self.timer_list = []
        self.current_timer_list = []
        self.current_label_list = []
        for i in range(12):
            _temp_timer = QTimer(self)
            _temp_timer.timeout.connect(lambda i=i: self.update_label(i))
            self.timer_list.append(_temp_timer)
        self.stop_timer = QTimer()
        self.stop_timer.timeout.connect(self.stop_update)
        self.pb_1.clicked.connect(lambda: self.prize_change(1))
        self.pb_2.clicked.connect(lambda: self.prize_change(2))
        self.pb_3.clicked.connect(lambda: self.prize_change(3))
        self.pb_4.clicked.connect(lambda: self.prize_change(4))
        self.pb_start.clicked.connect(self.start)
        self.pb_stop.clicked.connect(self.stop)
        self.pb_reset.clicked.connect(self.reset)
        self.label_list = [self.lbl_1, self.lbl_2, self.lbl_3, self.lbl_4, self.lbl_5, self.lbl_6, self.lbl_7,
                           self.lbl_8, self.lbl_9, self.lbl_10, self.lbl_11, self.lbl_12]
        self.init()

    def init(self):
        self.prize_change(1)
        self.level = 1
        # labels = find_all_labels(self)
        # for l in labels:
        #     l.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_1.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_2.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_3.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_4.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_5.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_6.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_7.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_8.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_9.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_10.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_11.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_12.setStyleSheet('background-color: rgba(255, 255, 255, 128);')

    def set_color(self, new_color):
        self.lbl_1.setStyleSheet(f'color: {new_color};')
        self.lbl_2.setStyleSheet(f'color: {new_color};')
        self.lbl_3.setStyleSheet(f'color: {new_color};')
        self.lbl_4.setStyleSheet(f'color: {new_color};')
        self.lbl_5.setStyleSheet(f'color: {new_color};')
        self.lbl_6.setStyleSheet(f'color: {new_color};')
        self.lbl_7.setStyleSheet(f'color: {new_color};')
        self.lbl_8.setStyleSheet(f'color: {new_color};')
        self.lbl_9.setStyleSheet(f'color: {new_color};')
        self.lbl_10.setStyleSheet(f'color: {new_color};')
        self.lbl_11.setStyleSheet(f'color: {new_color};')
        self.lbl_12.setStyleSheet(f'color: {new_color};')
    def reset(self):
        self.prize_list = []
        self.timer_count = 0
        self.level = 1
        self.prize_change(1)
        self.pt_list.clear()
        self.lottery_status = [True, True, True, True]
        self.set_color(gv.font_color[self.level - 1])

    def start(self):
        self.set_color(gv.font_color[self.level - 1])
        self.timer_count = 0
        music_url = QUrl('qrc:/bgm.MP3')
        self.player.setMedia(QMediaContent(music_url))
        self.player.play()
        for t in self.current_timer_list:
            t.start(50)
        self.pb_1.setEnabled(False)
        self.pb_2.setEnabled(False)
        self.pb_3.setEnabled(False)
        self.pb_4.setEnabled(False)
        self.pb_start.setEnabled(False)


    def stop(self):
        self.timer_count = 0
        self.stop_timer.start(500)

    def update_label(self, idx):
        num = [12, 6, 2, 1]
        idx_list = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 0, 0, 0, 1, 2, 3, 4, 5],
                    [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        random_numbers = random.sample(range(gv.start_number, gv.end_number + 1), num[self.level - 1])

        self.current_label_list[idx_list[self.level - 1][idx]].setText(
            str(random_numbers[idx_list[self.level - 1][idx]]))

    def stop_update(self):
        num_list = [12, 6, 2, 1]
        self.current_timer_list[self.timer_count].stop()
        num = 0
        while True:
            num = random.randint(gv.start_number, gv.end_number)
            if num not in self.prize_list:
                break
        self.prize_list.append(num)
        self.current_label_list[self.timer_count].setText(str(num))
        self.current_label_list[self.timer_count].setStyleSheet(f'color: red;')
        self.pt_list.appendPlainText(f"{gv.awards_name_list[self.level - 1]}:{num}")

        self.timer_count += 1
        if self.timer_count == num_list[self.level - 1]:
            self.stop_timer.stop()
            self.player.stop()
            self.lottery_status[self.level - 1] = True
            self.pb_1.setEnabled(True)
            self.pb_2.setEnabled(True)
            self.pb_3.setEnabled(True)
            self.pb_4.setEnabled(True)
            self.pb_start.setEnabled(True)

    def prize_change(self, level):
        self.level = level
        lbl_list = find_all_labels(self)
        for l in lbl_list:
            l.setStyleSheet(f'color: {gv.font_color[level - 1]};')
        self.centralwidget.setObjectName("wkWgt")  # 替换背景图片只对当前窗口生效 核心代码
        if not os.path.exists(gv.background_pic_list[level - 1]):
            self.centralwidget.setStyleSheet(f"#wkWgt{{border-image:url(:/b{level}.jpg);}}")
        else:
            self.centralwidget.setStyleSheet(f"#wkWgt{{border-image:url({gv.background_pic_list[level - 1]})}}")
        self.lbl_awards_level.setText(gv.awards_name_list[level - 1])
        self.lbl_prize_name.setText(gv.prize_name_list[level - 1])
        self.lbl_prize_name_2.setText(gv.prize_name_list_2[level - 1])
        if os.path.exists(gv.prize_pic_list[level - 1]):
            self.lbl_prize_pic.setPixmap(gv.prize_pic_list[level - 1])
        else:
            self.lbl_prize_pic.setPixmap(QPixmap(f":/{level}.svg"))
        if level == 1:

            self.current_timer_list = self.timer_list
            self.current_label_list = self.label_list
            self.pb_1.setEnabled(False)
            self.pb_2.setEnabled(True)
            self.pb_3.setEnabled(True)
            self.pb_4.setEnabled(True)
            self.lbl_1.setVisible(True)
            self.lbl_2.setVisible(True)
            self.lbl_3.setVisible(True)
            self.lbl_4.setVisible(True)
            self.lbl_5.setVisible(True)
            self.lbl_6.setVisible(True)
            self.lbl_7.setVisible(True)
            self.lbl_8.setVisible(True)
            self.lbl_9.setVisible(True)
            self.lbl_10.setVisible(True)
            self.lbl_11.setVisible(True)
            self.lbl_12.setVisible(True)
        elif level == 2:
            self.current_timer_list = self.timer_list[3:8 + 1]
            self.current_label_list = self.label_list[3:8 + 1]
            self.pb_1.setEnabled(True)
            self.pb_2.setEnabled(False)
            self.pb_3.setEnabled(True)
            self.pb_4.setEnabled(True)
            self.lbl_1.setVisible(False)
            self.lbl_2.setVisible(False)
            self.lbl_3.setVisible(False)
            self.lbl_4.setVisible(True)
            self.lbl_5.setVisible(True)
            self.lbl_6.setVisible(True)
            self.lbl_7.setVisible(True)
            self.lbl_8.setVisible(True)
            self.lbl_9.setVisible(True)
            self.lbl_10.setVisible(False)
            self.lbl_11.setVisible(False)
            self.lbl_12.setVisible(False)
        elif level == 3:
            self.current_timer_list = [self.timer_list[4], self.timer_list[7]]
            self.current_label_list = [self.label_list[4], self.label_list[7]]
            self.pb_1.setEnabled(True)
            self.pb_2.setEnabled(True)
            self.pb_3.setEnabled(False)
            self.pb_4.setEnabled(True)
            self.lbl_1.setVisible(False)
            self.lbl_2.setVisible(False)
            self.lbl_3.setVisible(False)
            self.lbl_4.setVisible(False)
            self.lbl_5.setVisible(True)
            self.lbl_6.setVisible(False)
            self.lbl_7.setVisible(False)
            self.lbl_8.setVisible(True)
            self.lbl_9.setVisible(False)
            self.lbl_10.setVisible(False)
            self.lbl_11.setVisible(False)
            self.lbl_12.setVisible(False)
        elif level == 4:
            self.current_timer_list = [self.timer_list[7]]
            self.current_label_list = [self.label_list[7]]
            self.pb_1.setEnabled(True)
            self.pb_2.setEnabled(True)
            self.pb_3.setEnabled(True)
            self.pb_4.setEnabled(False)
            self.lbl_1.setVisible(False)
            self.lbl_2.setVisible(False)
            self.lbl_3.setVisible(False)
            self.lbl_4.setVisible(False)
            self.lbl_5.setVisible(False)
            self.lbl_6.setVisible(False)
            self.lbl_7.setVisible(False)
            self.lbl_8.setVisible(True)
            self.lbl_9.setVisible(False)
            self.lbl_10.setVisible(False)
            self.lbl_11.setVisible(False)
            self.lbl_12.setVisible(False)
        if not self.lottery_status[level - 1]:
            for lbl in self.current_label_list:
                lbl.setText("")
        self.lbl_1.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_2.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_3.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_4.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_5.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_6.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_7.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_8.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_9.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_10.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_11.setStyleSheet('background-color: rgba(255, 255, 255, 128);')
        self.lbl_12.setStyleSheet('background-color: rgba(255, 255, 255, 128);')

    def closeEvent(self, event):
        gv.save_to_file("./config.txt")
        event.accept()

    def resizeEvent(self, event):
        self.showMaximized()
        super().resizeEvent(event)

