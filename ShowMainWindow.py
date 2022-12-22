import fitz
import os

from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow

from PIL import Image,ImageDraw,ImageFont

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("录用通知书生成器")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(self.width(),self.height())
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        #生成录取通知书
        self.pushButton.clicked.connect(self.create_picture)

    def create_picture(self):
        try:
            if self.lineEdit.text() == "":
                QtWidgets.QMessageBox.warning(self,"警告","请输入您的基本薪资")
            elif self.lineEdit_2.text() == "":
                QtWidgets.QMessageBox.warning(self,"警告","请输入年度目标奖金")
            else:
                QtWidgets.QMessageBox.information(self,"提示","生成成功")

            #获取基本薪资
            basic_salary = self.lineEdit.text()
            #获取年度目标奖金
            annual_bonus = self.lineEdit_2.text()

            pic = Image.open("1.png")
            #获取录取通知书的宽和高
            width = pic.size[0]
            height = pic.size[1]
            #获取录取通知书的宽和高的一半
            width_half = width / 2
            height_half = height / 2
            draw = ImageDraw.Draw(pic)
            font = ImageFont.truetype("FZCUJINLJW.ttf",120)
            font1 = ImageFont.truetype("FZL2JW.ttf",120)
            #添加标题
            draw.text((width_half-200,height_half-1500),"录用通知书",font=font,fill="#F7C77F")
            draw.text((width_half-1000,height_half-1200),f"您的基本薪资：{basic_salary}",font=font1,fill="#F7C77F")
            draw.text((width_half-1000,height_half-1000),f"年度目标奖金：{annual_bonus}",font=font1,fill="#F7C77F")

            #保存图片
            pic.save("录用通知书.png")

            imgdoc = fitz.open("录用通知书.png")
            pdfbytes = imgdoc.convert_to_pdf()
            imgdoc.close()
            imgpdf = fitz.open("录用通知书.pdf",pdfbytes)
            imgpdf.save("录用通知书.pdf")


        except Exception as e:
            print(e)
            pass




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

