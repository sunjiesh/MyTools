from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.textSource=QTextEdit()
        self.textSource.setObjectName("textSource")
        self.textPattern=QTextEdit()
        self.textPattern.setObjectName("textPattern")
        self.textResult=QTextBrowser()
        self.textResult.setObjectName("textaResult")
        formLayout=QFormLayout()
        formLayout.addWidget(self.textSource)
        formLayout.addWidget(self.textPattern)
        #formLayout.addWidget(self.textResult)

        mainLayout = QGridLayout()
        mainLayout.addLayout(formLayout, 0, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("RegexTester")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())
