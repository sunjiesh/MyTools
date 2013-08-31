#/bin/usr/python

from cn.com.sunjiesh.regextester.ui.MainWin import MainWindow


if __name__ == "__main__":
    import sys
    from PyQt4 import QtGui
    app = QtGui.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
