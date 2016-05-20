#!/usr/bin/python3


import sys
import re

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.initUI()


    def initUI(self):
        #Compements
        self.labelSource=QLabel()
        self.labelSource.setObjectName("labelSource")
        self.labelSource.setText("Source")
        self.textSource=QTextEdit()
        self.textSource.setObjectName("textSource")
        self.labelPattern=QLabel()
        self.labelPattern.setObjectName("labelPattern")
        self.labelPattern.setText("Pattern")
        self.textPattern=QTextEdit()
        self.textPattern.setObjectName("textPattern")
        self.labelResult=QLabel()
        self.labelResult.setObjectName("labelResult")
        self.labelResult.setText("Result")
        self.textResult=QTextBrowser()
        self.textResult.setObjectName("textaResult")
        self.btnRun = QPushButton()
        self.btnRun.setObjectName("btnRun")


        #Layout
        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QWidget(self.centralWidget)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.btnRun.setText("Run")

        self.btnRun.clicked.connect(self.on_btnRun_clicked)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.labelSource)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textSource)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.labelPattern)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textPattern)
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.btnRun)
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.labelResult)
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.textResult)

        self.setLayout(self.formLayout)

        self.setGeometry(300, 300, 800, 500)

    def on_btnRun_clicked(self):
        """
        执行验证操作，读取Source和Pattern，
        """
        #读取Source及Pattern
        textSource=self.textSource.toPlainText()
        textPattern=self.textPattern.toPlainText()
        if (textSource !="" and  textPattern!=""):
            textSource=str(textSource)
            textPattern=str(textPattern)
            print("textSource="+textSource)
            print("textPattern="+textPattern)
            #Regex验证
            result=""
            compileResult = re.findall(r""+textPattern, textSource)
            print("compileResult=",compileResult)
            if len(compileResult)>0:
                for resultItem in compileResult:
                    result=result+resultItem+"\n"
            else:
                result=u"没有找到符合条件的字符串"
                #result赋值
            self.textResult.setText(result)
        else:
            #提示弹出窗口
            QMessageBox.information(self,"錯誤", "请输入Source及Pattern")
            print("请输入Source及Pattern")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())
