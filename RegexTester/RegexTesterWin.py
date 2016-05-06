from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        #Compements
        self.textSource=QTextEdit()
        self.textSource.setObjectName("textSource")
        self.textPattern=QTextEdit()
        self.textPattern.setObjectName("textPattern")
        self.textResult=QTextBrowser()
        self.textResult.setObjectName("textaResult")

        #Layout
        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QRect(0, -10, 801, 601))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textSource)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textPattern)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textResult)
        self.setLayout(self.formLayout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())
