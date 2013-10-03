# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_MainWin import Ui_MainWindow

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
    def on_radioEncoder_clicked(self):
        """
        Slot documentation goes here.
        """
        print "on_radioEncoder_clicked"
    
    @pyqtSignature("")
    def on_radioDecoder_clicked(self):
        """
        Slot documentation goes here.
        """
        print "on_radioDecoder_clicked"
    
    @pyqtSignature("")
    def on_radioANSI_clicked(self):
        """
        Slot documentation goes here.
        """
        print "on_radioANSI_clicked"
    
    @pyqtSignature("")
    def on_radioUTF8_clicked(self):
        """
        Slot documentation goes here.
        """
        print "on_radioUTF8_clicked"
