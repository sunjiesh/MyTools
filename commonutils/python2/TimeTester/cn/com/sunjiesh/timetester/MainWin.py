# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_MainWin import Ui_MainWindow

import datetime
import time

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
    
    @pyqtSignature("bool")
    def on_btnConvert1_clicked(self, checked):
        """
        时间戳转换成北京时间，读取时间戳，如果有值，则生成时间，如果没有
        """
        timestampValue=self.txtTimestamp.toPlainText()
        if timestampValue=="":
            self.lblMessage.setText(u"时间戳为空")
        else:
            print timestampValue
            try:
                dt = datetime.datetime.fromtimestamp(float(timestampValue));
                print dt
                self.dateTimeEdit.setDateTime(dt)      
            except Exception, e:
                self.lblMessage.setText(u"转换时间错误")
                print e
                
        
        
    
    @pyqtSignature("bool")
    def on_btnConvert2_clicked(self, checked):
        """
        北京时间转换为时间戳
        """
        datetimeValue=self.dateTimeEdit.dateTime().toPyDateTime()
        try:
            print datetimeValue.timetuple()
            timestamp=time.mktime(datetimeValue.timetuple())
            timestamp=long(timestamp)
            self.txtTimestamp.setText(str(timestamp))
        except Exception, e:
                self.lblMessage.setText(u"转换时间错误")
                print e
            
