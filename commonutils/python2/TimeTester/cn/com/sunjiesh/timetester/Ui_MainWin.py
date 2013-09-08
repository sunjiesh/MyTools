# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tom/workspace/MyPythonApplicationA/commonutils-for-python/commonutils/python2/TimeTester/cn/com/sunjiesh/timetester/MainWin.ui'
#
# Created: Sun Sep  8 19:03:44 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 411, 146))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.btnConvert1 = QtGui.QPushButton(self.formLayoutWidget)
        self.btnConvert1.setObjectName(_fromUtf8("btnConvert1"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.btnConvert1)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txtTimestamp1 = QtGui.QTextEdit(self.formLayoutWidget)
        self.txtTimestamp1.setMinimumSize(QtCore.QSize(0, 10))
        self.txtTimestamp1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txtTimestamp1.setLineWidth(1)
        self.txtTimestamp1.setObjectName(_fromUtf8("txtTimestamp1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtTimestamp1)
        self.txtTime1 = QtGui.QTextBrowser(self.formLayoutWidget)
        self.txtTime1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txtTime1.setObjectName(_fromUtf8("txtTime1"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtTime1)
        self.formLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 140, 411, 142))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_3 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.btnConvert2 = QtGui.QPushButton(self.formLayoutWidget_2)
        self.btnConvert2.setObjectName(_fromUtf8("btnConvert2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.btnConvert2)
        self.txtTime2 = QtGui.QTextEdit(self.formLayoutWidget_2)
        self.txtTime2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txtTime2.setObjectName(_fromUtf8("txtTime2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtTime2)
        self.txtTimestamp2 = QtGui.QTextBrowser(self.formLayoutWidget_2)
        self.txtTimestamp2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txtTimestamp2.setObjectName(_fromUtf8("txtTimestamp2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtTimestamp2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "北京时间", None))
        self.btnConvert1.setText(_translate("MainWindow", "Unix时间戳转北京时间", None))
        self.label.setText(_translate("MainWindow", "Unix时间戳", None))
        self.label_3.setText(_translate("MainWindow", "北京时间", None))
        self.label_4.setText(_translate("MainWindow", "Unix时间戳", None))
        self.btnConvert2.setText(_translate("MainWindow", "北京时间转Unix时间戳", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

