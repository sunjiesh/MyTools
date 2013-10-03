# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_MainWin import Ui_MainWindow

import urllib

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
    def on_txtInput_textChanged(self):
        """
        Slot documentation goes here.
        """
        self.encodeAndDecode()
    
    @pyqtSignature("")
    def on_radioEncode_clicked(self):
        """
        Slot documentation goes here.
        """
        self.encodeAndDecode()
    
    @pyqtSignature("")
    def on_radioDecode_clicked(self):
        """
        Slot documentation goes here.
        """
        self.encodeAndDecode()
    
    @pyqtSignature("")
    def on_radioUTF8_clicked(self):
        """
        Slot documentation goes here.
        """
        self.encodeAndDecode()
        
    @pyqtSignature("")
    def on_radioANSI_clicked(self):
        """
        Slot documentation goes here.
        """
        self.encodeAndDecode()
        
    def encodeAndDecode(self):
        """
        Encode And Decode
        """
        inputStr=self.txtInput.toPlainText().toUtf8().__str__()
        if inputStr!="":
            print "before convert value is "+inputStr
            #operaMethod
            operaMethod="encode"
            if self.radioEncode.isChecked():
                operaMethod="encode"
            else:
                operaMethod="decode"
            print "operaMethod="+operaMethod
            #charset
            charset="gbk"
            if self.radioANSI.isChecked():
                charset="gbk"
            else:
                charset="utf8"
            print "charset="+charset
            
            outputStr=""
            try:
                if operaMethod=="encode":
                    outputStr=inputStr.decode("utf8").encode(charset)
                    m = {'':outputStr}
                    outputStr=urllib.urlencode(m)
                    outputStr=outputStr[1:]
                elif operaMethod=="decode":
                    outputStr="a".encode("gbk")
            except Exception, e:
                print e
                outputStr=u"convert error"
            print "outputStr="+outputStr 
            self.txtOutput.setPlainText(outputStr)
    
    
