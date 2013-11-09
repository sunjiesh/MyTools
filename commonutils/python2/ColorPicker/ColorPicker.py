# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4 import QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QMouseEvent
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import Qt

from PIL import Image


from Ui_ColorPicker import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("bool")
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
    def mousePressEvent(self,event):  
        if event.button()==Qt.LeftButton:  
            print "mouse press" 
        if event.button()==Qt.RightButton:  
            self.close()  
  
    def mouseMoveEvent(self,event): 
        """
            鼠标移动需要把鼠标的XY值读取，通过调用PIL实现
        """
        if event.buttons() & Qt.LeftButton:  
            pointX = event.globalX()
            pointY = event.globalY()
            print pointX
            # img is QImage type
            img = QPixmap.grabWindow(
                    QApplication.desktop().winId()).toImage()
            rgb = img.pixel(pointX, pointY)
            #十进制
            red10 = QtGui.qRed(rgb)
            green10 =QtGui.qGreen(rgb)
            blue10 = QtGui.qBlue(rgb)
            color10="("+str(red10)+","+str(green10)+","+str(blue10)+")"
            #十六进制
            red16=str(hex(red10))[2]
            if(len(red16)==1):
                red16="0"+red16
            green16=str(hex(green10))[2]
            if(len(green16)==1):
                green16="0"+green16
            blue16=str(hex(blue10))[2]
            if(len(blue16)==1):
                blue16="0"+blue16
            color16=red16+green16+blue16
            

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    colorDialog = Dialog()
    colorDialog.show()
    sys.exit(app.exec_())
