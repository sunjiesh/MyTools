# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_MainWin import Ui_MainWindow
from AlertDialog import AlertDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_btnRun_clicked(self):
        """
        执行验证操作，读取Source和Pattern，
        """
        #读取Source及Pattern
        textSource=self.textSource.toPlainText()
        textPattern=self.textPattern.toPlainText()
        if (textSource !="" and  textPattern!=""):
            print "textSource="+textSource
            print "textPattern="+textPattern
        else:
                alertDialog = AlertDialog()
                alertDialog.lblMessage.setText(u"请输入Source及Pattern");
                alertDialog.open ()
                alertDialog.exec_()
                print "请输入Source及Pattern"
