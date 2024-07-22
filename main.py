import os
import sys

from PySide6.QtGui import QIcon
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication
from frame.main_frame import MainWindowFrame
from func.global_value import gv
from ui.res_icon import qt_resource_data

if __name__ == '__main__':
    _temp = qt_resource_data
    os.environ['QT_API'] = 'pyside6'
    gv.init()
    gv.path = os.getcwd()
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication()
    app.setWindowIcon(QIcon(":/lottery.svg"))

    window = MainWindowFrame()
    window.showMaximized()
    sys.exit(app.exec())
