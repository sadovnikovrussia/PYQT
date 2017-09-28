from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import screen


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = screen.Ui_Dialog()
ui.setupUi(window)

'''
def test(ui):
    dir = os.getcwd() + '/screenshot'
    path = dir + '/screenshot.jpg'
    if not os.path.exists(dir):
        os.makedirs()
    QtGui.QPixmap.grabWindow(QtWidgets.QApplication.desktop().winId()).save(path,'jpg')
    pic = ui.label
    pic.setGeometry(10, 10, 450, 300)
    pic.setPixmap(QtGui.QPixmap(path))
    pic.setScaledContents(True)
'''

window.show()
sys.exit(app.exec_())
