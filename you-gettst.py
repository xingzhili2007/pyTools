from VipCode import *
import os
from you_get import common as you_get


class UI_Gold(PyQt5_QDialog):
    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(600, 400)
        self.setWindowTitle("视频解析器_Made-by-©李行之")
        self.setBackgroundColor('black')
        self.lable = PyQt5_Qlabel(self, 100, 40, 400, 100)
        # self.lable.setBackgroundColor('white')
        self.lable.setFontSize(40)
        self.lable.setText("   You-Get视频解析器")
        self.lable.setTextColor("white")
        self.lable1 = PyQt5_Qlabel(self, 10, 150, 120, 21)
        # self.lable1.setBackgroundColor('white')
        self.lable1.setTextColor('red')
        self.lable1.setText('输入网址或关键词:')
        self.edit = PyQt5_QLineEdit(self, 120, 150, 360)
        self.but = PyQt5_QPushButton(self, 505, 150, 50, 21)
        self.but.setText('确定')
        self.but.setBackgroundColor('brown')
        self.but.setTextColor('yellow')
        self.but.clicked.connect(lambda: self.gettext())

    def gettext(self):
        self.text = self.edit.text()
        QMessageBox.information(self, '提示信息', '你填写的网址是：' + self.text)
        print(self.text)
        QMessageBox.information(self, 'Warning', 'Are You Ready?')
        self.download(self.text)

    def download(self, url):
        now = os.getcwd()
        username = now.split('/')[2]
        path = "/Users/" + username + "/Downloads"
        sys.argv = ['you-get', "-o", path, url]
        you_get.main()
        os.system("open ~/Downloads")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()
