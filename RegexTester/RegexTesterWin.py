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
        self.btnRun = QPushButton()
        self.btnRun.setObjectName("btnRun")


        #Layout
        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QRect(0, -10, 801, 601))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.btnRun.setText("Run")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textSource)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textPattern)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.btnRun)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textResult)
        self.setLayout(self.formLayout)

    def on_btnRun_clicked(self):
        """
        执行验证操作，读取Source和Pattern，
        """
        #读取Source及Pattern
        textSource=self.textSource.toPlainText()
        textPattern=self.textPattern.toPlainText()
        if (textSource !="" and  textPattern!=""):
            textSource=unicode(textSource)
            textPattern=unicode(textPattern)
            print("textSource="+textSource)
            print("textPattern="+textPattern)
            #Regex验证
            result=""
            compileResult = re.findall(r""+textPattern, textSource)
        if len(compileResult)>0:
            for resultItem in compileResult:
                result=result+resultItem+"\n"
            else:
                result=u"没有找到符合条件的字符串"
            #result赋值
            self.textResult.setText(result)
        else:
            #提示弹出窗口
            QMessageBox.information(self, "请输入Source及Pattern")
        print("请输入Source及Pattern")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())
