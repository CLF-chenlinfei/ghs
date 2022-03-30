# ************************
# python version 3.7
# ************************
import os.path
import re
import sys
import threading
import time
import requests
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from pyqt5_plugins.examplebutton import QtWidgets

from PixivUi import Ui_Dialog
from spider import PV_Get_All_id, header, cook
import xvideos


# 按钮样式字符串参数
Bstr = "QPushButton{color:black}""QPushButton:hover{color:red}" \
      "QPushButton{background-color:lightgreen}" \
      "QPushButton{border:2px}""QPushButton{border-radius:5px}" \
      "QPushButton{padding:2px 4px}"


class Pix(QtWidgets.QMainWindow, QtWidgets.QWidget, Ui_Dialog):

    def __init__(self):
        super(Pix, self).__init__()
        self.setupUi(self)
        self.initUi()
        if os.path.exists("cookie.txt"):
            self.pushButton_cook.setVisible(False)
            self.textEdit.setText("Hello， 排行榜下载还没写！")
        else:
            self.textEdit.setText("若使用Pixiv画师下载，将这里的内容全部删除,\n再复制登陆后的Pixiv Cookie进这里点击保存Cookie!\n"
                                  "复制错了删除Cookie.txt重启程序再来一次!")

    def initUi(self):
        # 绑定按钮功能
        self.pushButton_hs.clicked.connect(self.on_pushButton_enter_clicked_hs)
        self.pushButton_ph.clicked.connect(self.on_pushButton_enter_clicked_ph)
        self.pushButton_gz.clicked.connect(self.on_pushButton_enter_clicked_gz)
        self.pushButton_xz.clicked.connect(self.download)
        self.pushButton_fpath.clicked.connect(self.msg)
        self.pushButton_cook.clicked.connect(self.save_cookies)

        # 设置按钮样式
        self.pushButton_fpath.setStyleSheet(Bstr)
        self.pushButton_ph.setStyleSheet(Bstr)
        self.pushButton_hs.setStyleSheet(Bstr)
        self.pushButton_gz.setStyleSheet(Bstr)
        self.pushButton_xz.setStyleSheet(Bstr)
        self.pushButton_cook.setStyleSheet(Bstr)

        # 部件透明的
        op = QtWidgets.QGraphicsOpacityEffect()
        op1 = QtWidgets.QGraphicsOpacityEffect()
        op2 = QtWidgets.QGraphicsOpacityEffect()
        op3 = QtWidgets.QGraphicsOpacityEffect()
        op4 = QtWidgets.QGraphicsOpacityEffect()
        op5 = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        op1.setOpacity(0.5)
        op2.setOpacity(0.5)
        op3.setOpacity(0.5)
        op4.setOpacity(0.5)
        op5.setOpacity(0.5)
        self.lineEdit_hsid_3.setGraphicsEffect(op1)
        self.lineEdit_hsid_2.setGraphicsEffect(op2)
        self.lineEdit_hsid.setGraphicsEffect(op3)
        self.lineEdit_path.setGraphicsEffect(op)
        self.textEdit.setGraphicsEffect(op5)
        self.comboBox.setGraphicsEffect(op4)

        # 文本框圆角设置
        self.lineEdit_hsid_3.setStyleSheet('''QLineEdit{border-radius:5px;}''')
        self.lineEdit_hsid_2.setStyleSheet('''QLineEdit{border-radius:5px;}''')
        self.lineEdit_hsid.setStyleSheet('''QLineEdit{border-radius:5px;}''')
        self.lineEdit_path.setStyleSheet('''QLineEdit{border-radius:5px;}''')
        self.textEdit.setStyleSheet('''QTextEdit{border-radius:5px;}''')
        self.comboBox.setStyleSheet('''QComboBox{border-radius:5px;}''')
        self.lineEdit_path.setText('D:\MyGui\pixivpageUer\\')
        self.path = self.lineEdit_path.text()

        palette = QPalette()
        # 背景像素宽度是650x480
        palette.setBrush(QPalette.Background,
                         QBrush(QPixmap("96921040_p0_master1200.jpg")))
        self.setPalette(palette)
        self.frame_hsym.setVisible(False)
        self.frame_gzym.setVisible(False)
        self.frame_phym.setVisible(False)
        self.lineEdit_hsid.setText('3384404')

    # 设置frame 可见
    def on_pushButton_enter_clicked_hs(self):
        self.frame_hsym.setVisible(True)
        self.frame_gzym.setVisible(False)
        self.frame_phym.setVisible(False)

    def on_pushButton_enter_clicked_ph(self):
        self.frame_hsym.setVisible(False)
        self.frame_gzym.setVisible(False)
        self.frame_phym.setVisible(True)

    def on_pushButton_enter_clicked_gz(self):
        self.frame_hsym.setVisible(False)
        self.frame_gzym.setVisible(True)
        self.frame_phym.setVisible(False)

    # 文件夹选区窗口
    def msg(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_path.setText(m)

    #Pixiv 画师页面
    def getPageImg(self, userid, newpath):
        url = "https://www.pixiv.net/artworks/%s" % userid
        try:
            req = requests.session()
            js = req.get(url, headers=header, cookies=cook).text
            title = re.search(r"\"illustTitle\":\"(.*?)\"", js).group(1)
            original = re.search(r"\"original\":\"(.*?)\"", js).group(1) # 能匹配到png
            pagecount = re.search(r"likeData.*?pageCount\":(\d+)", js).group(1)
            char_list = ['*', '|', ':', '?', '\/', '/', '<', '>', '"', '\\']
            for i in char_list:
                if i in title:
                    title = title.replace(i, "_")

            if pagecount == "1":
                rs = req.get(url=original, headers=header, timeout=(3, 4)).content
                with open(newpath + title+original[-6:], "ab") as f:
                    f.write(rs)

            else:
                if not os.path.exists(newpath+title):
                    os.makedirs(newpath+title)
                for i in range(int(pagecount)):
                    p = "p" + str(i)
                    nurl = original.replace("p0", p)
                    rs = req.get(url=nurl, headers=header, timeout=(3, 4)).content
                    with open(newpath + title + "\\" + title + nurl[-6:], "ab") as f:
                        f.write(rs)
        except:
            print(url)
            # self.textEdit.append("不能成功下载页面:%s" % url)
            pass
    #Pixiv 画师页面
    def get_user(self):
        try:
            start = time.time()
            allid = PV_Get_All_id(self.lineEdit_hsid.text())
            if not allid:
                self.textEdit.append("错误, 检查是否有cookie.txt，或者无外网！")
                return

            newpath = self.path + allid[1] + "\\"
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            allt = []
            for i in allid[0]:
                time.sleep(0.1)

                try:
                    t = threading.Thread(target=self.getPageImg, args=(i, newpath))
                    allt.append(t)
                    t.start()
                except:
                    pass
            for s in allt:
                s.join()
            finish = time.time() - start
            self.textEdit.append("画师:%s 下载完成!"
                                 "\n保存目录:%s \n总共用时:%.2f/S !"
                                 % (allid[1], newpath, finish))
        except:
            pass

    def XvideosSpider(self):
        tag = self.lineEdit_hsid_2.text()
        tr = []
        filepath = self.lineEdit_path.text()+"/"
        self.textEdit.append("开始下载Xvideos视频,标签:%s。" % tag)

        for i in xvideos.search(tag):
            t = threading.Thread(target=xvideos.XgetOnePage, args=(i['addUrl'], filepath + i['name']))
            t.start()
            tr.append(t)
            time.sleep(0.1)
        for i in tr:
            i.join()
        self.textEdit.append("Xvideos 标签:%s 视频下载结束!" % tag)

    def download(self):
        # Xvideos 视频下载
        if self.frame_gzym.isVisible():
            try:
                t = threading.Thread(target=self.XvideosSpider, args=())
                t.start()
            except:
                print("Xvideos 视频下载错误，检查是否未翻墙.")
        # pixiv画师下载
        if self.frame_hsym.isVisible():
            try:
                if self.frame_hsym.isVisible() and self.lineEdit_hsid.text() != "":
                    self.textEdit.append("开始下载画师:%s!" % self.lineEdit_hsid.text())
                    t = threading.Thread(target=self.get_user, args=())
                    t.start()
                else:
                    self.textEdit.append("Pixiv 下载错误，检查是否已翻墙!。")
            except:
                print("??")


        # 排行榜下载
        if self.frame_phym.isVisible():
            pass

    def save_cookies(self):
        cookies = self.textEdit.toPlainText()
        with open('cookie.txt', "w") as f:
            f.write(cookies)
        self.pushButton_cook.setVisible(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Pix()
    window.show()
    sys.exit(app.exec_())