# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tom/workspace/MyPythonApplicationA/commonutils-for-python/commonutils/python2/Code/cn/com/sunjiesh/code/MainWin.ui'
#
# Created: Thu Oct  3 18:04:26 2013
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
        MainWindow.resize(543, 332)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 9, 531, 301))
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
        self.plainTextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_9.addWidget(self.plainTextEdit)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.radioEncoder = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioEncoder.setObjectName(_fromUtf8("radioEncoder"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.radioEncoder)
        self.radioDecoder = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioDecoder.setObjectName(_fromUtf8("radioDecoder"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.radioDecoder)
        self.verticalLayout_9.addLayout(self.formLayout)
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
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.verticalLayout_10.addWidget(self.plainTextEdit_2)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.radioANSI = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioANSI.setObjectName(_fromUtf8("radioANSI"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.radioANSI)
        self.radioUTF8 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioUTF8.setObjectName(_fromUtf8("radioUTF8"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.radioUTF8)
        self.verticalLayout_10.addLayout(self.formLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Input", None))
        self.radioEncoder.setText(_translate("MainWindow", "Encoder", None))
        self.radioDecoder.setText(_translate("MainWindow", "Decoder", None))
        self.label_2.setText(_translate("MainWindow", "Output", None))
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

