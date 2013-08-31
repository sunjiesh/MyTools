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

import re

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
            #Regex验证
            result=""
            compileResult = re.findall(r""+str(textPattern), textSource)
            if len(compileResult)>0:
                for resultItem in compileResult:
                    result=result+resultItem+"\n"
            else:
                result="没有找到符合条件的字符串"
            #result赋值
            self.textResult.setText(result)
        else:
                #提示弹出窗口
                alertDialog = AlertDialog()
                alertDialog.lblMessage.setText(u"请输入Source及Pattern");
                alertDialog.open ()
                alertDialog.exec_()
                print "请输入Source及Pattern"
