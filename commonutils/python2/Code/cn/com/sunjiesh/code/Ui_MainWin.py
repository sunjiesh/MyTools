# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tom/workspace/MyPythonApplicationA/commonutils-for-python/commonutils/python2/Code/cn/com/sunjiesh/code/MainWin.ui'
#
# Created: Thu Oct  3 21:13:12 2013
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
        MainWindow.resize(596, 380)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 9, 591, 341))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_9.addWidget(self.label)
        self.txtInput = QtGui.QPlainTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtInput.sizePolicy().hasHeightForWidth())
        self.txtInput.setSizePolicy(sizePolicy)
        self.txtInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txtInput.setObjectName(_fromUtf8("txtInput"))
        self.verticalLayout_9.addWidget(self.txtInput)
        self.groupBox = QtGui.QGroupBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(30, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 220, 80))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioEncode = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioEncode.setObjectName(_fromUtf8("radioEncode"))
        self.horizontalLayout.addWidget(self.radioEncode)
        self.radioDecode = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioDecode.setObjectName(_fromUtf8("radioDecode"))
        self.horizontalLayout.addWidget(self.radioDecode)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_10.addWidget(self.label_2)
        self.txtOutput = QtGui.QPlainTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOutput.sizePolicy().hasHeightForWidth())
        self.txtOutput.setSizePolicy(sizePolicy)
        self.txtOutput.setObjectName(_fromUtf8("txtOutput"))
        self.verticalLayout_10.addWidget(self.txtOutput)
        self.groupBox_2 = QtGui.QGroupBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 20, 216, 80))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioANSI = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioANSI.setObjectName(_fromUtf8("radioANSI"))
        self.horizontalLayout_2.addWidget(self.radioANSI)
        self.radioUTF8 = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioUTF8.setObjectName(_fromUtf8("radioUTF8"))
        self.horizontalLayout_2.addWidget(self.radioUTF8)
        self.verticalLayout_10.addWidget(self.groupBox_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Input", None))
        self.groupBox.setTitle(_translate("MainWindow", "Opera", None))
        self.radioEncode.setText(_translate("MainWindow", "Encode", None))
        self.radioDecode.setText(_translate("MainWindow", "Decode", None))
        self.label_2.setText(_translate("MainWindow", "Output", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Chatset", None))
        self.radioANSI.setText(_translate("MainWindow", "ANSI", None))
        self.radioUTF8.setText(_translate("MainWindow", "UTF8", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

