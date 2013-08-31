# -*- coding: utf-8 -*-

"""
Module implementing AlertDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_AlertDialog import Ui_Dialog

class AlertDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_btnConfirm_clicked(self):
        """
        关闭Dialog
        """
        self.setVisible(False)
