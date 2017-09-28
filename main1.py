from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp
from PyQt5.QtCore import QSize
import gui, sys

app = QApplication(sys.argv)
ui = gui.MainWindow()
ui.show()
#ui.setWindowTitle('Тестовая программа')
sys.exit(app.exec_())