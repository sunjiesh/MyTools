# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tom/workspace/MyPythonApplicationA/commonutils-for-python/commonutils/python2/RegexTester/cn/com/sunjiesh/regextester/ui/AlertDialog.ui'
#
# Created: Sat Aug 31 13:24:14 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.lblMessage = QtGui.QLabel(Dialog)
        self.lblMessage.setGeometry(QtCore.QRect(40, 100, 311, 17))
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.btnConfirm = QtGui.QPushButton(Dialog)
        self.btnConfirm.setGeometry(QtCore.QRect(130, 180, 87, 27))
        self.btnConfirm.setObjectName(_fromUtf8("btnConfirm"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblMessage.setText(_translate("Dialog", "Message", None))
        self.btnConfirm.setText(_translate("Dialog", "confirm", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

