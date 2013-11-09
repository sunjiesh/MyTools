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
            鼠标移动需要把鼠标的XY值读取
        """
        if event.buttons() & Qt.LeftButton:  
            pointX = event.globalX()
            pointY = event.globalY()
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
            #print str(hex(red10))
            red16=str(hex(red10))[2:]
            green16=str(hex(green10))[2]
            blue16=str(hex(blue10))[2:]
            color16=red16+green16+blue16
            #print color16
            print "(%s,%s) = %s (%s,%s,%s)" % (pointX, pointY, color16,red10, green10, blue10)
            self.label.setText("(%s,%s) = %s (%s,%s,%s)" % (pointX, pointY, color16,red10, green10, blue10))
            

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    colorDialog = Dialog()
    colorDialog.show()
    sys.exit(app.exec_())
